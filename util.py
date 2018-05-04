"""
util.py - just a simple place to pack all the useful functions
that I might need.
"""
import contextlib
from datetime import datetime as dt
import os
import traceback
import xxhash


def dump_object(obj, offset='\t'):
    """
    Dump the output of a protobuf message
    """
    for descriptor in obj.DESCRIPTOR.fields:
        value = getattr(obj, descriptor.name)
        if descriptor.type == descriptor.TYPE_MESSAGE:
            if descriptor.label == descriptor.LABEL_REPEATED:
                map(dump_object, value)
            else:
                dump_object(value)
        elif descriptor.type == descriptor.TYPE_ENUM:
            enum_name = descriptor.enum_type.values[value].name
            print("{0}{1}: {2}".format(offset, descriptor.full_name, enum_name))
        else:
            print("{0}{1}: {2}".format(offset, descriptor.full_name, value))


def getCfg(filename=None):
    """
    This handles the setup for the config parser and all that
    """
    import configparser
    config = filename
    if config is None:
        config = getConfigFile()
    cfg = configparser.ConfigParser()
    cfg.read(config)
    cfg.set('server', 'cfgfile', config)

    return cfg


def getConfigFile():
    """
    returns the location of the configuration file.
    """
    final = os.path.dirname(os.path.realpath(__file__))
    final = os.path.join(final, '../etc')
    config = None
    for loc in os.curdir, \
            os.path.expanduser('~'), \
            '/etc/', \
            os.environ.get('SERVER_CONF'), \
            final:
        try:
            config = os.path.join(loc, 'server.ini')
        except AttributeError:
            pass
        if config is not None and os.path.exists(config):
            return config
    return None


def getTracebackInfo(inst):
    """
    Single function to take an 'Exception' instance and return the
    traceback information.  This function is mainly used for logging
    purposes
    """
    emsg = 'Traceback:\n'
    for line in traceback.format_exc().splitlines():
        emsg += '{0}\n'.format(line)
    return emsg


def getAnswer(prompt='?', choices=['yes', 'no']):
    """
    Prompt the user for a response.  Continue asking the user until we get
    a valid response
    """
    ans = raw_input(prompt)
    while ans not in choices:
        ans = raw_input(prompt)
    return ans


def printHeader(items=[], spacing=[], sep='-', indent="  "):
    """
    Simple way to print a header and separator programmatically
    """
    if len(items) != len(spacing):
        raise IndexError("items and spacing are not equal length arrays")
    x = 0          # loop control variable
    fstr = indent  # formatted string
    tc = 0         # total character count
    for item in items:
        tc += spacing[x]   # calculate the total characters in the header
        tstr = "{0}:{1}".format(x, spacing[x])
        fstr += '{' + "{0}".format(tstr) + "} "
        x += 1
    # display header
    print(fstr.format(*items))

    # display the separator
    hr = indent
    for i in xrange(tc):
        hr += sep
    print(hr)
