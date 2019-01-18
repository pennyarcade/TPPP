"""
Implements a non interactive controller for terminal.

Useful for displaying unattended presentations.
"""

from time import sleep

from tpp import FileParser
from tpp.controller import TPPController
from tpp.visualizer import TPPVisualizer


class AutoplayController(TPPController):
    """
    Implements a non interactive controller for terminal.

    Useful for displaying unattended presentations.
    """

    def __init__(self, filename, secs, visualizer_class: TPPVisualizer):
        """
        Todo: ApiDoc.

        :param filename:
        :param secs:
        :param visualizer_class:
        """
        self.filename = filename
        # Todo: Check how to do this reflection thing correctly
        self.vis = visualizer_class
        self.seconds = secs
        self.cur_page = 0
        self.reload_file = False
        self.pages = []

    def close(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.vis.close()

    def run(self):
        """
        Todo: ApiDoc.

        :return: None
        """
        while True:
            self.reload_file = False
            parser = FileParser(self.filename)
            self.pages = parser.get_pages()
            if self.cur_page >= len(self.pages):
                self.cur_page = len(self.pages) - 1
            self.vis.clear()
            self.vis.new_page()
            self.do_run()
            if not self.reload_file:
                break

    def do_run(self):
        """
        Todo: ApiDoc.

        :return:
        """
        while True:
            wait = False
            self.vis.draw_slidenum(self.cur_page + 1, len(self.pages), False)
            # read and visualize lines until the visualizer says "stop" or we reached the end of the page
            while True:
                # emulate do..until
                line = self.pages[self.cur_page].next_line()
                eop = self.pages[self.cur_page].is_eop()
                wait = self.vis.visualize(line, eop)

                if wait or eop:
                    break

            # draw slide number on the bottom left and redraw
            self.vis.draw_slidenum(self.cur_page + 1, len(self.pages), eop)
            self.vis.do_refresh()

            if eop:
                if self.cur_page + 1 < len(self.pages):
                    self.cur_page += 1
                else:
                    self.cur_page = 0

                self.pages[self.cur_page].reset_eop()
                self.vis.new_page()

            sleep(self.seconds)
