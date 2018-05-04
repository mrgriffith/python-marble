"""
DMAServer
    base class for processes
"""

import logging
import logging.config
import os
import socket
import sys

import streamtologger


class Server(object):
    def __init__(self, cfg, daemonize=True):
        """
        all servers need logging, so let's set everything up in the base
        class
        """
        # setup logging
        logging.config.fileConfig(cfg.get('server', 'cfgfile'))
        self._logger = logging.getLogger(cfg.get('server', 'default_logger'))
        self._cfg = cfg

        if daemonize:
            # log stdout/stderr to a logger
            myLogger = streamtologger.StreamToLogger(self._logger)
            sys.stdout = myLogger
            sys.stderr = myLogger

        # identification information
        self._pid = os.getpid()
        self._host = socket.getfqdn()
        self._id = '{0}:{1}'.format(self._host, self._pid)
        self._name = self.__class__.__name__
        self._server_name = "{0}({1})".format(self._name, self._id)

    def __del__(self):
        """
        Log that the process is shutting down
        """
        # If we added the process, then we need to cleanup
        #self._logger.info("Server '{0}' Stopped.".format(self._server_name))
        pass

    def join(self):
        pass

    def run(self,):
        pass

    def start(self):
        """
        Start a server as a daemon
        """
        msg = "Starting Server '{0}' now ...".format(self._server_name)
        self._logger.info(msg)
        # start the server
        self.run()

    def getServerName(self):
        """
        return the server's name
        """
        return self._server_name
