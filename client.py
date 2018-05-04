#!/usr/bin/env python

"""
Simple client to test functionality
"""

import argparse
import time
from datetime import datetime
from threading import Thread

import util
import CMN_MAPI_pb2
import Connection
import DMA_MAPI_pb2


def generateMessage(msg,
                    filename=None,
                    token=58438,
                    outgoing=True,
                    requestid=None,
                    area=None,
                    emails=None,
                    permissions=None):
    """
    Generate a message to be passed to the broker
    """
    msg.header.token = token
    msg.header.err_code = 0
    msg.request_id = requestid

    return msg


def main():
    """
    connect to the server and pass a request
    """
    fmtclass = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=fmtclass)
    parser.add_argument('-s', '--server', default='tcp://localhost:7010',
                        help="broker connection string")
    parser.add_argument('-t', '--token', default=1234, type=int,
                        help="token string")
    parser.add_argument('-r', '--requestid', default=None, type=int,
                        help="specify a request id")
    parser.add_argument('--times', action='store_true', default=False,
                        help="display times")
    args = parser.parse_args()

    #  Socket to talk to server
    c = Connection.Connection(a_address=args.server, a_mode='CLIENT')
    c.registerProtocol(DMA_MAPI_pb2)
    c.registerProtocol(CMN_MAPI_pb2)

    msg = None
    # construct message
    msg = DMA_MAPI_pb2.Msg_Archive()
    msg.header.token = args.token
    msg.header.err_code = 0
    msg.request_id = args.requestid


    if msg is not None:
        if args.times:
            print("{0} ".format(datetime.now()))
        print("Sending: ")
        util.dump_object(msg)
        print(" ")
        # send the request
        c.send(msg)

        # Get the ACK First
        done = False
        while not done:
            # get the response, should be a 'status' message
            res = c.recv()
            if res[0] is not None:
                if c.getMessageTypeName(res[0]) == 'Msg_Ack':
                    if args.times:
                        print("{0} ".format(datetime.now()))
                    print("Received ACK:")
                    util.dump_object(res[1])
                    print(" ")
                    done = True
            else:
                print(res)
    else:
        print("msg is none")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
