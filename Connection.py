import google.protobuf.reflection
import zmq
import struct
import time

SERVER=0
CLIENT=1
PUBLISHER=2
SUBSCRIBER=3
WORKER=4
BOSS=5
mode = {SERVER: 'SERVER', 'SERVER': SERVER,
        CLIENT: 'CLIENT', 'CLIENT': CLIENT,
        PUBLISHER: 'PUBLISHER', 'PUBLISHER': PUBLISHER,
        SUBSCRIBER: 'SUBSCRIBER', 'SUBSCRIBER': SUBSCRIBER,
        WORKER: 'WORKER', 'WORKER': WORKER,
        BOSS: 'BOSS', 'BOSS': BOSS,
       }

class Connection:
    """
    Initialize a Connection object
    """
    def __init__(self,
                 a_address=None,
                 a_host=None,
                 a_port=None,
                 a_mode=CLIENT,
                 a_context=None,
                 a_trirecv=False):

        if a_mode not in mode:
            raise zmq.ZMQError("Invalid Connection mode: '{0}'".format(a_mode))
        elif isinstance(a_mode, str):
            a_mode = mode[a_mode]
        self._mode = a_mode
        # Caller can provide either an address (e.g., 'inproc://foo',
        # 'tcp://localhost:99', etc.) or a hostname and port number.
        if a_address is None and a_host and a_port:
            a_address = self.host_port_address(a_host, a_port)
        elif a_address is None:
            raise zmq.ZMQError('One of address or host+port is required')
        elif a_address and (a_host or a_port):
            raise zmq.ZMQError('Only one of address or host+port is allowed')

        self._msg_desc_by_type = {}
        self._msg_type_by_desc = {}
        self._proc_addresses = False
        self._trirecv = a_trirecv

        # init zeromq
        if a_context:
            self._context = a_context
            self._context_owner = False
        else:
            self._context = zmq.Context()
            self._context_owner = True
            self._context.setsockopt( zmq.RECONNECT_IVL, 2000 )


        self._address = a_address
        if a_mode == SERVER:
            self._proc_addresses = True
            self._socket = self._context.socket( zmq.ROUTER )
            self.setupKeepAlive()
            self._socket.bind( a_address )
        elif a_mode == CLIENT:
            self._socket = self._context.socket( zmq.DEALER )
            self.setupKeepAlive()
            self._socket.connect( a_address )
        elif a_mode == PUBLISHER:
            self._socket = self._context.socket( zmq.PUB )
            self.setupKeepAlive()
            self._socket.bind( a_address )
        elif a_mode == SUBSCRIBER:
            self._socket = self._context.socket( zmq.SUB )
            self.setupKeepAlive()
            self._socket.connect( a_address )
            self._socket.setsockopt_string(zmq.SUBSCRIBE, u'')
        elif a_mode == BOSS:
            self._proc_addresses = True
            self._socket = self._context.socket( zmq.DEALER )
            self.setupKeepAlive()
            self._socket.bind( a_address )
        elif a_mode == WORKER:
            self._proc_addresses = True
            self._socket = self._context.socket( zmq.DEALER )
            self.setupKeepAlive()
            self._socket.connect( a_address )

        self._socket.setsockopt(zmq.LINGER, 100)

    # -------------------------------------------------------------------------
    def __del__(self):
        """
        Delete/cleanup a CDS API instance
        """
        if '_socket' in dir(self):
            self._socket.close()
        if '_context' in dir(self) and self._context_owner:
            self._context.destroy()

    # -------------------------------------------------------------------------
    @classmethod
    def host_port_address(cls, host, port):
        """
        Assemble and return a TCP address based on a host name and port number
        """
        rval = 'tcp://{0}:{1}'.format(host, port)
        return rval

    # -------------------------------------------------------------------------
    def setupKeepAlive( self ):
        self._socket.setsockopt( zmq.TCP_KEEPALIVE, 1 )
        self._socket.setsockopt( zmq.TCP_KEEPALIVE_CNT, 20 )
        self._socket.setsockopt( zmq.TCP_KEEPALIVE_IDLE, 540 )
        self._socket.setsockopt( zmq.TCP_KEEPALIVE_INTVL, 5 )

    # -------------------------------------------------------------------------
    def registerProtocol( self, a_msg_module ):
        """
        Must build a message type (integer) to descriptor table for automatic
        message creation/parsing on receive
        """
        # Message descriptors are stored by name - must convert to an array in definition order
        msgs_by_start = {}
        for name, desc in a_msg_module.DESCRIPTOR.message_types_by_name.items():
            msgs_by_start[desc._serialized_start] = desc

        # build descriptors by type look-up
        proto_id = a_msg_module._PROTOCOL.values[0].number;
        idx = 0
        for i,desc in sorted(msgs_by_start.items()):
            self._msg_desc_by_type[(proto_id << 16)|idx] = desc;
            idx += 1

        # build indexes
        idx = proto_id << 16
        for i,desc in sorted(msgs_by_start.items()):
            #print idx, ' @ ', desc
            self._msg_desc_by_type[idx] = desc;
            self._msg_type_by_desc[desc] = idx;
            idx += 1

    # -------------------------------------------------------------------------
    def recv( self, a_timeout=1000 ):
        """
        Receive a protobuf message with timeout (may throw zeromq/protobuf exceptions)
        """
        # Wait for data to arrive
        rval = []
        ready = self._socket.poll( a_timeout )
        if ready > 0:
            if self._proc_addresses:
                ident = self._socket.recv( zmq.NOBLOCK )
                rval.append(ident)
            elif self._trirecv:
                rval.append(None)

            # receive zermq frame header and unpack
            frame_data = self._socket.recv( zmq.NOBLOCK )
            frame_values = struct.unpack( '<HHL', frame_data )
            msg_type = (frame_values[0] << 16) | frame_values[1]

            # receive message paylod into buffer
            data = self._socket.recv( zmq.NOBLOCK )

            # find message descriptor based on type (descriptor index)
            desc = self._msg_desc_by_type[msg_type]

            # make new instance of message subclass and parse from buffer
            rval.append(msg_type)
            rval.append(google.protobuf.reflection.ParseMessage( desc, data ))
            return rval
        elif self._proc_addresses or self._trirecv:
            return None, 0, None
        else:
            return 0, None

    # -------------------------------------------------------------------------
    def send( self, a_message, route=None ):
        """
        Sends a protobuf message (may throw zeromq/protobuf exceptions)
        """
        # Find msg type by descriptor look-up
        msg_type = self._msg_type_by_desc[a_message.DESCRIPTOR]

        # Reverse word order
        msg_type = (msg_type & 0xFFFF << 16) | (msg_type & 0xFFFF0000 >> 16)

        # Serialize
        data = a_message.SerializeToString()
        # Build the message frame, to match C-struct MessageFrame
        frame = struct.pack( '<HHL', msg_type >> 16, msg_type & 0xFFFF, len( data ))
        # Send frame, then body
        if self._proc_addresses:
            print("In PROC: ", str(route))
            self._socket.send( route, zmq.NOBLOCK | zmq.SNDMORE)
        while True:
            try:
                self._socket.send( frame, zmq.NOBLOCK | zmq.SNDMORE )
                break
            except zmq.Again:
                time.sleep(0.1)
        while True:
            try:
                self._socket.send( data, zmq.NOBLOCK )
                break
            except zmq.Again:
                time.sleep(0.1)


    # -------------------------------------------------------------------------
    def getMessageTypeName( self, a_msg_type ):
        """
        Return the short name of a message class based on message type
        """
        # if a_msg_type > 0 and a_msg_type < self._msg_desc_by_type:
        #     return self._msg_desc_by_type[a_msg_type].name
        # return ''
        if a_msg_type in self._msg_desc_by_type:
            rval = self._msg_desc_by_type[a_msg_type].name
        else:
            rval = ''
        return rval
