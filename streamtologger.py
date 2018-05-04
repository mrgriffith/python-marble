"""
I was looking for a way to have a deamon log stdout and stderr to
a logger python builtin.  This way everything goes to one file.

After some googling, I ended up at Ferry Boender's blog:
http://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/

This appears to give me what I want
"""

import logging


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self,):
        """
        Needed to add this function when trying to use multiprocessing.Process
        """
        pass
