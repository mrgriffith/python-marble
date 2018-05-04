#!/usr/bin/env python
"""
The Broker
"""
import random
import zmq

import Connection
import CMN_MAPI_pb2
import DMA_MAPI_pb2
from server import Server


class Broker(Server):
    """
    The Broker class
    """

    def __init__(self, cfg):
        """
        Constructor -
            sets the server/broker address and boss address
        """
        super(self.__class__, self).__init__(cfg)
        # ################  Setup ZMQ  ############################
        self._server = Connection.Connection(a_mode='SERVER',
                                  a_address="tcp://*:7010")
        self._server.registerProtocol(DMA_MAPI_pb2)
        self._server.registerProtocol(CMN_MAPI_pb2)

        # Poller
        self._poll = zmq.Poller()
        self._poll.register(self._server._socket, zmq.POLLIN)
        random.seed()

    def run(self):
        """
        Run the Broker Server
        """
        rm = ['Hi There', 'How Are You?', 'Want to play a game?']
        
        while True:
            sockets = dict(self._poll.poll(5000))

            if self._server._socket in sockets and \
                sockets[self._server._socket] == zmq.POLLIN:
                msg = self._server.recv()
                if msg[0] is not None:
                    print(msg)
                    self._logger.debug("Msg {0} received".format(msg))
                    ack = CMN_MAPI_pb2.Msg_Ack()
                    ack.header.token = msg[2].header.token
                    ack.header.err_code = 0
                    ack.header.err_msg = random.choice(rm)
                    self._server.send(ack, msg[0])


if __name__ == '__main__':
    import util
    cfg = util.getCfg()
    print("CFG: {0}".format(cfg.get('server', 'cfgfile')))
    a = Broker(cfg)
    a.start()
