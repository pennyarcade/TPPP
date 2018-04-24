"""
Set up and run the program

Todo: ApiDoc
"""
import argparse
import sys

from tpp import Switch
from tpp.controller import AutoplayController, ConversionController, InteractiveController
from tpp.visualizer import NCursesVisualizer, TextVisualizer, LatexVisualizer


class TPPRunner(object):
    """
    Set up and run the program

    Todo: ApiDoc
    """
    def __init__(self, args=sys.argv):
        """
        Todo: ApiDoc
        """
        self.version_number = "1.3.1"
        self.args = args
        self.input = None
        self.output = None
        self.type = 'ncurses'
        self.controller = None

    def parse_args(self, parser_class=argparse.ArgumentParser):
        """
        Create argument parser, handle command line parameters, provide command line help.

        Avoid a global default configuration by setting default values here.
        Factory method

        @see: https://stackoverflow.com/questions/39028204/using-unittest-to-test-argparse-exit-errors

        :param parser_class: set the argument parser class in an optional parameter to be able to switch it out for testing
        :return:
        """
        parser = parser_class('TPPP - Text Presentation Program Python Edition')

        parser.add_argument(
            'input',
            help='TPPP presentation source file',
            metavar='file',
            type=lambda s: s.strip()
        )

        parser.add_argument(
            '-v',
            '--version',
            help='Print version and exit',
            action='store_true'
        )

        parser.add_argument(
            '-t',
            '--type',
            help='set file type for output format',
            choices=[],
            type=lambda s: s.strip().lower()
        )

        parser.add_argument(
            '-o',
            '--output',
            help='set file to write output to',
            type=lambda s: s.strip()
        )

        parser.add_argument(
            '-s',
            '--seconds',
            help='wait <seconds> between slides (with -t autoplay)',
            type=int
        )

        self.config = parser.parse_args(self.args)

    def validate_args(self):
        """
        validate the commadline arguments; sanity checks

        :return:
        """
        # Todo: Implement
        pass

    def configure(self):
        """
        configure the program for running

        Todo: make visualizer configurable or auto detect instead of hardcoded

        :return:
        """
        for case in Switch(self.type):
            if case('autoplay'):
                self.load_ncurses()
                self.controller = AutoplayController(self.input, NCursesVisualizer)
                break
            if case('text'):
                self.controller = ConversionController(self.input, self.output, TextVisualizer)
            if case('latex'):
                self.controller = ConversionController(self.input, self.output, LatexVisualizer)
            if case():
                self.load_ncurses()
                self.controller = InteractiveController(self.input, NCursesVisualizer)

    def run(self):
        """
        run the program

        Todo: ApiDoc

        :return:
        """
        self.parse_args()
        self.validate_args()
        self.configure()
        self.controller.run()
        self.controller.close()

    def load_ncurses(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass
