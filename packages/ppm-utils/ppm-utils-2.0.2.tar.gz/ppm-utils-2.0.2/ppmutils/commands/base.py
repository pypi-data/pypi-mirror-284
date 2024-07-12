"""The base command."""

import os
import sys
import time
import requests
from enum import Enum
from furl import furl

from ppmutils import couleur

import logging
logger = logging.getLogger('ppmutils')


class Style(Enum):
    """ An enum of colors for console output. """
    Error = 'red'
    Warning = 'yellow'
    Info = 'blue'
    Debug = 'white'
    Success = 'green'
    Important = 'orange'


class Shell(object):
    """A class for facilitating output of status/progress to the shell"""

    shell = None

    def __init__(self):

        # Init the shell
        self.shell = couleur.Shell(linebreak=False, indent=4)

    def __getattr__(self, attr):
        """
        If this class doesn't implement said attr, pass it through to the lower shell
        """
        # Check message types
        for style in Shell.Style:
            if style.name.lower() == attr:
                # Return the color
                return getattr(self.shell, style.value)

        return getattr(self.shell, attr)

    def print(self, message, n=False, style=Style.Debug):
        """
        Prints a message to the console with the corresponding coloring
        :param message: The message to display
        :param n: Whether to automatically line break or not
        :param style: The shell style/color
        :return: None
        """
        try:
            getattr(self.shell, style.value)(message)

            # Check newline
            if n:
                self.shell.white('\n')

        except Exception as e:
            self.shell.red('Error: {}'.format(e))

    def println(self, message, style=Style.Debug):
        """
        Prints a message to the console with the corresponding coloring and newline
        :param message: The message to display
        :param style: The shell style/color
        :return: None
        """
        self.print(message, n=True, style=style)

    def progress(self, message, length=5, n=True, style=Style.Debug):
        """
        Shows a message and then blocks while showing a little progress indicator
        :param message: The message to show before progress
        :param length: How long to block in seconds
        :param n: Whether to automatically line break or not
        :param style: The shell style/color
        :return: None
        """
        # Pause
        self.print('{} '.format(message), style=style)
        for i in range(length * 2):
            self.print('.', style=style)
            sys.stdout.flush()
            time.sleep(0.5)
        if n:
            self.shell.white('\n')

    def header(self, title, subtitle=None, style=Style.Info):
        """
        Outputs a section header to distinguish the current process from prior output
        :param title: The title of the current section
        :param subtitle: The description of this section
        :param style: The shell style/color
        :return: None
        """

        # Output a header
        self.print('{}\n'.format('-' * 120))
        self.print('{}\n'.format('-' * 120))
        self.print('\n{}: '.format(title.upper()), style=style)
        if subtitle:
            self.print('{}\n\n'.format(subtitle))
        else:
            self.print('\n\n')
        self.print('{}\n'.format('-' * 120))
        self.print('{}\n\n'.format('-' * 120))

    def prompt(self, message, default=None, style=Style.Info):
        """
        Prompts the user with the given message and returns their response
        :param message: The message for the prompt
        :param default: The default answer that should be shown, if any
        :param style: The shell style/color
        :return: boolean
        """
        # Determine prompt text
        if default:
            prompt = ' ({}): '.format(default)
        else:
            prompt = ': '

        while True:
            self.print(message, style=style)
            response = input(prompt).lower()
            if not response and default:
                return default
            elif not response:
                self.print('Please enter your response', n=True, style=Shell.Style.Error)
            else:
                return response

    def yes_no(self, message, default=None, style=Style.Info):
        """
        Prompts the user with the given message and returns their response
        :param message: The message for the prompt
        :param default: The default answer that should be shown/returned
        :param style: The shell style/color
        :return: boolean
        """
        yes = ['yes', 'y', 'ye', '1', 'true', 't']
        no = ['no', 'n', '0', 'false', 'f']

        # Determine prompt text
        if default is not None:
            prompt = ' ({}): '.format(yes[0] if default else no[0])
        else:
            prompt = ': '

        while True:
            self.print(message, style=style)
            choice = input(prompt).lower()
            if choice in yes:
                return True
            elif choice in no:
                return False
            elif not choice and default is not None:
                return default
            else:
                self.print('Please enter a valid response', n=True, style=Shell.Style.Error)


class Base(object):
    """A base command."""

    url = None
    shell = None

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.url = options['--url']

        # Get a couleur shell
        self.shell = Shell()

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def query_bundle(self, resource_type, query=None):
        """
        This method will fetch all resources for a given type, including paged results.
        :param resource_type: FHIR resource type
        :type resource_type: str
        :param query: A dict of key value pairs for searching resources
        :type query: dict
        :return: A Bundle of FHIR resources
        :rtype: Bundle
        """
        # Build the URL.
        url_builder = furl(self.url)
        url_builder.path.add(resource_type)

        # Add query if passed and set a return count to a high number,
        # despite the server
        # probably ignoring it.
        url_builder.query.params.add("_count", 1000)
        if query is not None:
            for key, value in query.items():
                if type(value) is list:
                    for _value in value:
                        url_builder.query.params.add(key, _value)
                else:
                    url_builder.query.params.add(key, value)

        # Prepare the final URL
        query_url = url_builder.url

        # Collect them.
        total_bundle = None

        # The url will be set to none on the second iteration if all resources
        # were returned, or it will be set to the next page of resources if more exist.
        while query_url is not None:

            # Make the request.
            response = requests.get(query_url)
            response.raise_for_status()

            # Parse the JSON.
            bundle = response.json()
            if total_bundle is None:
                total_bundle = bundle
            elif bundle.get("total", 0) > 0:
                total_bundle["entry"].extend(bundle.get("entry"))

            # Check for a page.
            query_url = None

            for link in bundle.get("link", []):
                if link["relation"] == "next":
                    query_url = link["url"]

        return bundle.get("entry", [])
