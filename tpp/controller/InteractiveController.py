"""
Implements an interactive controller.

It which feeds the visualizer until it is told to stop and then reads a key press
and executes the appropriate action.
"""

from tpp.FileParser import FileParser
from tpp.Switch import Switch
from tpp.controller.TPPController import TPPController
from tpp.visualizer.TPPVisualizer import TPPVisualizer


class InteractiveController(TPPController):
    """
    Implements an interactive controller.

    It feeds the visualizer until it is told to stop and then reads a key press
    and executes the appropriate action.
    """

    def __init__(self, input_stream, output_stream, visualizer_class: TPPVisualizer):
        """
        Initialize Controller.

        Todo: ApiDoc

        :param input_stream:
        :param output_stream:
        :param visualizer_class:
        """
        self.file = input_stream
        print(self.file)
        self.vis = visualizer_class
        self.cur_page = 0
        self.reload_file = False
        self.pages = None

    def close(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.vis.close()

    def run(self):
        """
        Todo: ApiDoc.

        :return:
        """
        while True:
            self.reload_file = False
            parser = FileParser(self.file)
            self.pages = parser.get_pages()
            if self.cur_page >= len(self.pages):
                self.cur_page = len(self.pages) - 1
            self.vis.clear
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

            # read a character from the keyboard
            # a "break" in the when means that it breaks the loop, i.e. goes on with visualizing lines
            while True:
                char = self.vis.get_key()
                for case in Switch(char):
                    if case('q', 'Q'):  # (Q)uit
                        return
                    if case('r', 'R'):  # (R)edraw slide
                        changed_page = True
                        # @Todo: actuaklly implement redraw
                    if case('e', 'E'):
                        self.cur_page = len(self.pages) - 1
                        break
                    if case('s', 'S'):
                        self.cur_page = 0
                        break
                    if case('j', 'J'):  # (J)ump to slide
                        screen = self.vis.store_screen()
                        new_page = self.vis.read_newpage(self.pages, self.cur_page)
                        if 0 <= new_page < len(self.pages):
                            self.cur_page = new_page
                            self.pages[self.cur_page].reset_eop()
                            self.vis.new_page()
                        else:
                            self.vis.restore_screen(screen)
                        break
                    if case('l', 'L'):  # re(l)oad current file
                        self.reload_file = True
                        return
                    if case('c', 'C'):  # (c)ommand prompt
                        screen = self.vis.store_screen()
                        self.vis.do_command_prompt()
                        self.vis.clear()
                        self.vis.restore_screen(screen)
                    if case(':keyright', ':keydown', ' '):  # next slide
                        if self.cur_page + 1 < len(self.pages) and eop:
                            self.cur_page += 1
                            self.pages[self.cur_page].reset_eop()
                            self.vis.new_page()
                        break
                    if case('b', 'B', ':keyleft', ':keyup'):
                        if self.cur_page > 0:
                            self.cur_page -= 1
                            self.pages[self.cur_page].reset_eop()
                            self.vis.new_page()
                        break
                    if case(':keyresize'):
                        self.vis.setsizes()
