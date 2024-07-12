"""
ppm-utils

Usage:
  ppm-utils fixresearchsubjects --url <url> [-v|-vv|-vvv|-vvvv]
  ppm-utils fixflags --url <url> [-v|-vv|-vvv|-vvvv]
  ppm-utils -h | --help
  ppm-utils --version
  ppm-utils [-v|-vv|-vvv|-vvvv]

Options:
  -h --help                             Show this screen.
  -u <url>, --url <url>                 The FHIR service URL.
  -v, --verbose                         Show verbose Ansible output up to 4 options
                                        level 1 : Show error messages
                                        level 2 : Show warning messages
                                        level 3 : Show info messages
                                        level 4 : Show all messages
Examples:
  ppm-utils fixflags --url https://fhir.ppm.aws.dbmi.hms.harvard.edu/baseDstu3
  ppm-utils fixresearchsubjects --url https://fhir.ppm.aws.dbmi-loc.hms.harvard.edu/baseDstu3

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/hms-dbmi/ppm-utils.git
"""


from inspect import getmembers, isclass

from docopt import docopt
import logging
from colorlog import ColoredFormatter

from . import __version__ as VERSION
from ppmutils.commands import base


def setup_logger(options):
    """Return a logger with a default ColoredFormatter."""
    formatter = ColoredFormatter(
        "%(log_color)s%(message)-8s%(reset)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'bold_red',
        }
    )

    logger = logging.getLogger('ppmutils')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Determine log level
    if options['--verbose'] == 1:
        logging.disable(logging.WARNING)
    elif options['--verbose'] == 2:
        logging.disable(logging.INFO)
    elif options['--verbose'] == 3:
        logging.disable(logging.DEBUG)

    return logger


def main():
    """Main CLI entrypoint."""
    import os
    import ppmutils.commands

    options = docopt(__doc__, version=VERSION)

    # Setup logging.
    logger = setup_logger(options)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(ppmutils.commands, k) and v:
            module = getattr(ppmutils.commands, k)
            module_name = f'{module.__package__}.{k}'
            command = next(iter(getmembers(module, lambda cmd: isclass(cmd) and issubclass(cmd, base.Base) and cmd.__module__ == module_name)))[1]
            command = command(options)
            command.run()
