"""
Implement a visualizer which converts TPP source to a nicely formatted text file.

Which can e.g. be used as handout.

Todo: ApiDoc
"""

import os
import textwrap

from tpp.visualizer.TPPVisualizer import TPPVisualizer


class TextVisualizer(TPPVisualizer):
    """
    Implement a visualizer which converts TPP source to a nicely formatted text file.

    Which can e.g. be used as handout.

    Todo: ApiDoc
    """

    def __init__(self, outputfile):
        """
        Todo: ApiDoc.

        :param outputfile: file
        """
        self.file_handle = outputfile
        self.output_env = False
        self.title = False
        self.author = False
        self.date = False
        self.figlet_font = 'small'
        self.width = 80

    def do_footer(self, footer_text):
        """
        Todo: ApiDoc.

        :param footer_text:
        :return:
        """
        pass

    def do_header(self, header_text):
        """
        Todo: ApiDoc.

        :param header_text:
        :return:
        """
        pass

    def do_refresh(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def new_page(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.file_handle.write('------------------------------------------------------------' + os.linesep)

    def do_heading(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        with self.file_handle.write as puts:
            puts(os.linesep)
            for line in textwrap.wrap(text, self.width):
                puts(line + os.linesep)
            puts('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + os.linesep)

    def do_with_border(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_hor_line(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.file_handle.write('************************************************************' + os.linesep)

    def do_color(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        pass

    def do_exec(self, cmdline):
        """
        Todo: ApiDoc.

        :param cmdline:
        :return:
        """
        pass

    def do_wait(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_begin_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.file_handle.write('.-------------------------------------')
        self.output_env = True

    def do_begin_shell_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.do_begin_output()

    def do_end_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.file_handle.write('\'-------------------------------------')
        self.output_env = False

    def do_end_shell_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.do_end_output()

    def do_sleep(self, seconds):
        """
        Todo: ApiDoc.

        :param seconds:
        :return:
        """
        pass

    def do_bold_on(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_bold_off(self):
        """
        Todo: ApiDoc.

        :return:
        """

    def do_rev_on(self):
        """
        Todo: ApiDoc.

        :return:
        """

    def do_command_prompt(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_rev_off(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_ul_on(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_ul_off(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_begin_slide_left(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_end_slide(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_begin_slide_right(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_begin_slide_bottom(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_begin_slide_top(self):
        """
        Todo: ApiDoc.

        :return:
        """
        pass

    def do_set_huge_font(self, params):
        """
        Todo: ApiDoc.

        :param params:
        :return:
        """
        self.figlet_font = params

    def do_huge(self, text):
        """
        Todo: ApiDoc.

        Todo: fix code duplication

        :param text:
        :return:
        """
        output_width = self.width
        if self.output_env:
            output_width -= 2
        output_handle = os.popen("figlet -f %s -w %d -k %s" % (self.figlet_font, output_width, text), 'r')
        for line in output_handle.readlines():
            self.print_line(line)
        output_handle.close()

    def print_line(self, text: str):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        for line in textwrap.wrap(text, self.width):
            if self.output_env:
                self.file_handle.write("| %s%s" % (line, os.linesep))
            else:
                self.file_handle.write(line + os.linesep)

    def do_center(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        for line in textwrap.wrap(text, self.width):
            spaces = (self.width - len(line)) / 2
            if spaces < 0:
                spaces = 0
            self.print_line(' ' * spaces + line)

    def do_right(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        for line in textwrap.wrap(text, self.width):
            spaces = (self.width - len(line))
            if spaces < 0:
                spaces = 0
            self.print_line(' ' * spaces + line)

    def do_title(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        self.file_handle.write("Title: %s" % text)
        self.title = True
        if self.title and self.author and self.date:
            self.file_handle.write(os.linesep * 2)

    def do_author(self, text: str):
        """
        Todo: ApiDoc.

        :param text: str
        :return:
        """
        self.file_handle.write("Author: %s" % text)
        self.author = True
        if self.title and self.author and self.date:
            self.file_handle.write(os.linesep * 2)

    def do_date(self, text: str):
        """
        Todo: ApiDoc.

        :param text: str
        :return:
        """
        self.file_handle.write("Date: %s" % text)
        self.date = True
        if self.title and self.author and self.date:
            self.file_handle.write(os.linesep * 2)

    def do_bg_color(self, color):
        """
        Todo: ApiDoc.

        :param color:
        :return:
        """
        pass

    def do_fg_color(self, color):
        """
        Todo: ApiDoc.

        :param color:
        :return:
        """
        pass

    def close(self):
        """
        Todo: ApiDoc.

        :return:
        """
        self.file_handle.close()
