"""
Implement a visualizer which converts TPP source to a nicely formatted text file which can e.g. be used as handout

Todo: ApiDoc
"""

import os
import sys
import textwrap

from tpp.visualizer.TPPVisualizer import TPPVisualizer


class TextVisualizer(TPPVisualizer):
    """
    Implement a visualizer which converts TPP source to a nicely formatted text file which can e.g. be used as handout

    Todo: ApiDoc
    """
    def __init__(self, outputfile):
        """
        Todo: ApiDoc

        :param outputfile:
        """
        self.filename = outputfile
        try:
            self.filehandle = open(self.filename, os.O_WRONLY)
        except IOError as exc:
            sys.stderr.write("Error: could not open file for writing: %s" % self.filename)
            sys.exit(1)
            # Todo: better error message
        self.output_env = False
        self.title = False
        self.author = False
        self.date = False
        self.figletfont = 'small'
        self.width = 80

    def do_footer(self, footer_text):
        """
        Todo: ApiDoc

        :param footer_text:
        :return:
        """
        pass

    def do_header(self, header_text):
        """
        Todo: ApiDoc

        :param header_text:
        :return:
        """
        pass

    def do_refresh(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def new_page(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.filehandle.write('------------------------------------------------------------' + os.linesep)

    def do_heading(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        with self.filehandle.write as puts:
            puts( + os.linesep)
            for line in textwrap.wrap(text, self.width):
                puts(line + os.linesep)
            puts('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + os.linesep)

    def do_withborder(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_horline(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.filehandle.write('************************************************************' + os.linesep)

    def do_color(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        pass

    def do_exec(self, cmdline):
        """
        Todo: ApiDoc

        :param cmdline:
        :return:
        """
        pass

    def do_wait(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_begin_output(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.filehandle.write('.-------------------------------------')
        self.output_env = True

    def do_begin_shell_output(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.do_begin_output()

    def do_end_output(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.filehandle.write('\'-------------------------------------')
        self.output_env = False

    def do_end_shell_output(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.do_end_output()

    def do_sleep(self, seconds):
        """
        Todo: ApiDoc

        :param seconds:
        :return:
        """
        pass

    def do_bold_on(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_bold_off(self):
        """
        Todo: ApiDoc

        :return:
        """

    def do_rev_on(self):
        """
        Todo: ApiDoc

        :return:
        """

    def do_command_prompt(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_rev_off(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_ul_on(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_ul_off(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_begin_slide_left(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_end_slide(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_begin_slide_right(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_begin_slide_bottom(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_begin_slide_top(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_set_huge_font(self, params):
        """
        Todo: ApiDoc

        :param params:
        :return:
        """
        self.figletfont = params

    def do_huge(self, text):
        """
        Todo: ApiDoc
        Todo: fix code duplication

        :param text:
        :return:
        """
        output_width = self.width
        if self.output_env:
            output_width -= 2
        op = os.popen("figlet -f %s -w %d -k %s" % (self.figletfont, width, text), 'r')
        for line in op.readlines():
            self.print_line(line)
        op.close()

    def print_line(self, line):
        """
        Todo: ApiDoc

        :param line:
        :return:
        """
        for line in textwrap.wrap(line, self.width):
            if self.output_env:
                self.filehandle.write("| %s%s" % (line, os.linesep))
            else:
                self.filehandle.write(line + os.linesep)

    def do_center(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        for line in textwrap.wrap(line, self.width):
            spaces = (self.width -len(line)) / 2
            if spaces < 0:
                spaces = 0
            self.print_line(' ' * spaces + line)

    def do_right(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        for line in textwrap.wrap(line, self.width):
            spaces = (self.width - len(line))
            if spaces < 0:
                spaces = 0
            self.print_line(' ' * spaces + line)

    def do_title(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.filehandle.write("Title: %s" % text)
        self.title = True
        if self.title and self.author and self.date:
            self.filehandle.write(os.linesep * 2)

    def do_author(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.filehandle.write("Author: %s" % text)
        self.author = True
        if self.title and self.author and self.date:
            self.filehandle.write(os.linesep * 2)

    def do_date(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.filehandle.write("Date: %s" % text)
        self.date = True
        if self.title and self.author and self.date:
            self.filehandle.write(os.linesep * 2)

    def do_bgcolor(self, color):
        """
        Todo: ApiDoc

        :param color:
        :return:
        """
        pass

    def do_fgcolor(self, color):
        """
        Todo: ApiDoc

        :param color:
        :return:
        """
        pass

    def close(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.filehandle.close()
