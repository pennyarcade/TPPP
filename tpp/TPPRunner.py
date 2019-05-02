"""
Set up and run the program.

Todo: ApiDoc
"""
import argparse
import sys
import curses
from pydoc import locate

from tpp import Switch


class TPPRunner:
    """
    Set up and run the program.

    Todo: ApiDoc
    """

    def __init__(self, args=None):
        """Todo: ApiDoc."""
        self.version_number = "1.3.1"
        if args is None:
            self.args = sys.argv
        else:
            self.args = args
        self.input_stream = None
        self.output_stream = None
        self.controller = None
        self.config = None
        self.parser = None
        self.configure_parser()

    def configure_parser(self, parser_class=argparse.ArgumentParser):
        """
        Create argument parser, handle command line parameters, provide command line help.

        Avoid a global default configuration by setting default values here.
        Factory method

        @see: https://stackoverflow.com/questions/39028204/using-unittest-to-test-argparse-exit-errors

        :param parser_class: set the argument parser class in an optional param to be able to switch it out for testing
        :return:
        """
        self.parser = parser_class(prog='tppp', description='TPPP - Text Presentation Program Python Edition')

        self.parser.add_argument(
            'tpp_source_file',
            metavar='source_file',
            type=argparse.FileType('r', encoding='UTF-8', errors='replace'),
            nargs='?',
            help='TPP presentation source file',
            default=None
        )

        self.parser.add_argument(
            '-v',
            '--version',
            help='Print version and exit',
            action='store_true'
        )

        self.parser.add_argument(
            '-t',
            '--type',
            help='set file type for output format',
            choices=['latex', 'autoplay', 'text'],
            type=lambda s: s.strip().lower()
        )

        self.parser.add_argument(
            '-o',
            '--output',
            help='set file to write output to',
            type=lambda s: s.strip()
        )

        self.parser.add_argument(
            '-s',
            '--seconds',
            help='wait <seconds> between slides (with -t autoplay)',
            type=int
        )

    def validate_args(self):
        """
        Validate the command line arguments and perform sanity checks.

        :return:
        """
        if self.config.version:
            print('TPPP Version %s' % self.version_number)
            print()
            self.parser.print_usage()
            sys.exit(0)

        if self.config.tpp_source_file is None:
            self.parser.error('the following arguments are required: source_file')

    def configure(self):
        """
        Configure the program for running.

        Todo: make visualizer configurable or auto detect instead of hardcoded
        Todo: unify controller interface to extract class instanciation

        :return TPPController:
        """
        for case in Switch(self.config.type):
            if case('autoplay'):
                controller_class = locate('tpp.controller.AutoplayController')
                visualizer_class = locate('tpp.visualizer.NCursesVisualizer')
                self.controller = controller_class(self.input_stream, visualizer_class())
                break
            if case('text'):
                controller_class = locate('tpp.controller.ConversionController')
                visualizer_class = locate('tpp.visualizer.TextVisualizer')
                self.controller = controller_class(self.input_stream, self.output_stream, visualizer_class())
                break
            if case('latex'):
                controller_class = locate('tpp.controller.ConversionController')
                visualizer_class = locate('tpp.visualizer.LatexVisualizer')
                self.controller = controller_class(self.input_stream, self.output_stream, visualizer_class())
                break
            if case():
                controller_class = locate('tpp.controller.InteractiveController')
                visualizer_class = locate('tpp.visualizer.NCursesVisualizer')

                from pprint import pprint
                pprint(controller_class)
                pprint(visualizer_class)

                self.controller = controller_class(self.input_stream, self.output_stream, visualizer_class())

                break

    def run(self):
        """
        Run the program.

        Todo: ApiDoc

        :return:
        """
        try:
            self.config = self.parser.parse_args()
            self.validate_args()
            self.configure()
            self.controller.run()
            self.controller.close()
        except Exception as exc:
            curses.nocbreak()
            # stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            raise exc
