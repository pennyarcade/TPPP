"""
Implements a visualizer which converts TPP source to LaTeX-Beamer source
@see http://latex-beamer.sf.net
"""

import os
import sys

import textwrap

from tpp.visualizer.TPPVisualizer import TPPVisualizer


class LatexVisualizer(TPPVisualizer):
    """
    Implements a visualizer which converts TPP source to LaTeX-Beamer source
    @see http://latex-beamer.sf.net
    Todo: convert this one later
    """
    def __init__(self, output_file):
        """
        Todo: ApiDoc

        :param output_file:
        """
        self.filename = output_file
        try:
            self.file_handle = open(self.filename, os.O_WRONLY)
        except IOError:
            sys.stderr.write("Error: Could not open file %s%s" % (self.filename, os.linesep))
            sys.exit(1)

        self.slide_open = False
        self.verbatim_open = False
        self.width = 50
        self.title, self.date, self.author = False
        self.begin_doc = False
        self.file_handle.writelines([
            "% Filename:     %s" % os.path.basename(self.filename),
            "% Purpose:      TPPP Latex export",
            "% Author:       ",
            "% License:      ",
            "% Latest change: Fre Apr 15 20:32:37 CEST 2005",
            "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",
            "",
            "\documentclass{beamer}",
            "",
            "\mode<presentation>",
            "{",
            "  \usetheme{Montpellier}",
            "  \setbeamercovered{transparent}",
            "}",
            "",
            "\usepackage[german]{babel}",
            "\usepackage{umlaut}",
            "\usepackage[latin1]{inputenc}",
            "\usepackage{times}",
            "\usepackage[T1]{fontenc}",
            ""
        ])

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

    def try_close(self):
        """
        Todo: ApiDoc

        :return:
        """
        if self.verbatim_open:
            self.file_handle.write("\end{verbatim}" + os.linesep)
            self.verbatim_open = False
        if self.slide_open:
            self.file_handle.write("\end{frame}" + os.linesep)
            self.slide_open = False

    def new_page(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.try_close()

    def do_heading(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.try_close()
        self.file_handle.write("\\section{%s}" % text)

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
        pass

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
        # Todo: implement output tuff
        pass

    def do_begin_shell_output(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_end_output(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

    def do_end_shell_output(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass

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
        pass

    def do_huge(self, text):
        """
        Todo: ApiDoc
        Todo: fix code duplication

        :param text:
        :return:
        """
        pass

    def try_open(self):
        """
        Todo: ApiDoc

        :return:
        """
        if not self.begin_doc:
            self.file_handle.write("\\begin{document}")
            self.begin_doc = True
        if not self.slide_open:
            self.file_handle.write("\\begin{frame}[fragile]")
            self.slide_open = True
        if not self.verbatim_open:
            self.file_handle.write("\\begin{verbatim}")
            self.begin_doc = True

    def try_intro(self):
        """
        Todo: ApiDoc

        :return:
        """
        if self.author and self.title and self.date:
            if not self.begin_doc:
                self.file_handle.write("\\begin{document}")
                self.begin_doc = True
            self.file_handle.writelines([
                "\\begin{frame}",
                "\\titlepage",
                "\\end{frame}"
            ])

    def print_line(self, line):
        """
        Todo: ApiDoc

        :param line:
        :return:
        """
        self.try_open()
        for line in textwrap.wrap(line, self.width):
            self.file_handle.write(line + os.linesep)

    def do_center(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        pass

    def do_right(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        pass

    def do_title(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.file_handle.write("\\title[%s]{%s}" % (text, text))
        self.title = True

    def do_author(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.file_handle.write("\\author{%s}" % text)
        self.author = True

    def do_date(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.file_handle.write("\\date{%s}" % text)
        self.date = True

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
        self.try_close()
        self.file_handle.write("\\end{document}")
        self.file_handle.write("%%%%% END OF FILE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        self.file_handle.close()
