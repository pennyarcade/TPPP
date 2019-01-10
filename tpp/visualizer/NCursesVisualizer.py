import curses
import os
import random
import textwrap
import re
from time import sleep

from tpp.ColorMap import ColorMap
from tpp.visualizer.TPPVisualizer import TPPVisualizer


class NCursesVisualizer(TPPVisualizer):
    """
        Implements an interactive visualizer which builds on top of NCurses
    """

    def __init__(self):
        """
        Todo: ApiDoc
        """
        self.figletfont = "standard"

        self.screen = curses.initscr()
        curses.curs_set(0)
        curses.cbreak()  # unbuffered input
        curses.noecho()  # turn off input echoing
        curses.qiflush(False)
        self.screen.keypad(True)

        self.setsizes()

        curses.start_color()
        curses.use_default_colors()
        self.do_bgcolor('black')
        self.do_fgcolor("white")
        self.fgcolor = ColorMap.get_color_pair('white')
        self.voffset = 5
        self.indent = 3
        self.cur_line = self.voffset
        self.output = False
        self.shelloutput = False
        self.termwidth = 0
        self.termheight = 0
        self.withborder = False
        self.slideoutput = False
        self.slidedir = "LEFT"
        self.fgcolor = None

    def get_key(self):
        """
        Todo: ApiDoc

        :return string: Character or special key reference
        """
        ch = self.screen.getch()

        if ch == curses.KEY_RIGHT:
            return ':keyright'
        elif ch == curses.KEY_DOWN:
            return ':keydown'
        elif ch == curses.KEY_LEFT:
            return ':keyleft'
        elif ch == curses.KEY_UP:
            return ':keyup'
        elif ch == curses.KEY_RESIZE:
            return ':keyresize'

        return ch

    def clear(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.clear()
        self.screen.refresh()

    def setsizes(self):
        """
        Todo: ApiDoc
        Todo: How to do this with python curses

        :return:
        """
        # self.termwidth = get nax screen size
        # self.termheight = get max screen height
        pass

    def do_refresh(self):
        """
        Todo: ApiDoc

        :return: None
        """
        self.screen.refresh()

    def do_withborder(self):
        """
        Todo: ApiDoc

        :return: None
        """
        self.withborder = True
        draw_border()

    def do_command_prompt(self):
        """
        Todo: ApiDoc

        :return: None
        """
        message = "Press any key to continue..."
        curser_pos = 0
        max_len = 50
        prompt = "tpp@localhost:~ $ "
        string = ""

        # Todo: How to do this in python curses?
        # window = self.screen.dupwin()
        # curses.overwrite(window, self.screen)  # overwrite screen with window

        curses.curs_set(1)
        curses.echo()

        # window.move(self.termheight/4, 1)
        # window.clrtoeol()
        # window.clrtobot()
        # window.mvaddstr(self.termheight/4, 1, prompt) # add the prompt string

        while True:
            # window.mvaddstr(self.termheight/4, 1 + len(prompt), string) # add the code
            # window.move(self.termheight/4, 1 + len(prompt) + cursor_pos) # move cursor to the end of the code
            ch = window.getch()

            if ch in [curses.KEY_ENTER, "\n", "\r"]:
                curses.curs_set(0)
                curses.noecho()
                rc = os.system(string)
                if not rc:
                    self.screen.mvaddstr(
                        self.termheight / 4, 1, "Error: Exec \"%s\" failed with error code #%s" % (string, rc)
                    )
                    self.screen.mvaddstr(
                        self.termheight - 2, self.termwidth / 2 - len(message) / 2, message
                    )
                else:
                    self.screen.mvaddstr(
                        self.termheight - 2, self.termwidth / 2 - len(message) / 2, message
                    )
                    ch = self.screen.getch()
                    self.screen.refresh
                    return
            elif ch == curses.KEY_LEFT:
                curser_pos = max(0, curser_pos - 1)  # jump one character to the left
            elif ch == curses.KEY_RIGHT:
                curser_pos = max(0, curser_pos + 1)  # jump one character to the left
            elif ch == curses.KEY_BACKSPACE:
                # Todo: check range expressions
                string = string[0, max(0, curser_pos - 1)] + string[curser_pos, -1]
                curser_pos = max(0, curser_pos - 1)
                window.mvaddstr(
                    self.termheight / 4, 1 + len(prompt) + len(string), " "
                )
            # Todo: How does this expression work in python?
            elif " ": #[0]..255:
                if curser_pos < max_len:
                    string[curser_pos, 0] = chr(ch)
                    curser_pos += 1
                else:
                    curses.beep()
            else:
                curses.beep()

        curses.curs_set(0)

    def draw_border(self):
        """
        Todo: ApiDoc

        :return: None
        """
        with self.screen as s:
            s.move(0,0)

            s.addstr('.')
            s.addstr((self.termwidth - 2) * '-')
            s.addstr("'")

            for y in range(1, self.termheight - 3):
                s.move(y, 0)
                s.addstr('|')
                s.move(y, self.termwidth - 1)
                s.addstr('|')

    def new_page(self):
        """
        Todo: ApiDoc

        :return: None
        """
        self.cur_line = self.voffset
        self.output = False
        self.shelloutput = False
        self.setsizes()
        self.screen.clear()

    def do_heading(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.screen.attron(curses.A_BOLD)
        self.print_heading(text)
        self.screen.attroff(curses.A_BOLD)

    def do_horline(self):
        """
        Todo: ApiDoc

        :return:
        """
        with self.screen as s:
            s.attron(curses.A_BOLD)
            s.move(self.cur_line, 0)
            s.addstr('-' * self.termwidth)
            s.attroff(curses.A_BOLD)

    def print_heading(self, text):
        """
        Todo: ApiDoc

        :param width:
        :return:
        """
        width = self.termwidth - 2 * self.indent
        with self.screen as s:
            for line in textwrap.wrap(text, width):
                # Todo: is this line superfluous?
                # s.move(self.cur_line, self.indent)
                s.move(self.cur_line, self.termwidth - len(line) / 2)
                s.addstr(line)
                self.cur_line += 1

    def do_center(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        width = self.termwidth - 2 * self.indent
        if self.output or self.shelloutput:
            width -= 2

        with self.screen as s:
            for line in textwrap.wrap(text, width):
                s.move(self.cur_line, self.indent)
                if self.output or self.shelloutput:
                    s.addstr(' |')
                s.move(self.cur_line, (self.termwidth - self.indent) / 2)
                s.addstr(line)
                if self.output or self.shelloutput:
                    s.addstr(' |')
                self.cur_line += 1

    def do_right(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        width = self.termwidth - 2 * self.indent
        if self.output or self.shelloutput:
            width -= 2

        with self.screen as s:
            for line in textwrap.wrap(text, width):
                s.move(self.cur_line, self.indent)
                if self.output or self.shelloutput:
                    s.addstr(' |')
                s.move(self.cur_line, self.termwidth - len(line) - 5)
                s.addstr(line)
                if self.output or self.shelloutput:
                    s.addstr(' |')
                self.cur_line += 1

    def show_help_page(self):
        help_text = "\n".join([
            'TPP help',
            '',
            'space bar ............................... display next entry within page',
            'space bar, cursor-down, cursor-right .... display next page',
            'b, B, cursor-up, cursor-left ............ display previous page',
            'q, Q .................................... quit TPP',
            'j, J .................................... jump directly to page',
            'l, L .................................... reload current file',
            's, S .................................... jump to the first page',
            'e, E .................................... jump to the last page',
            'c, C .................................... start command line',
            '?, h, H ................................. this help screen',
        ])
        with self.screen as s:
            s.clear()
            y = self.voffset
            for line in help_text:
                s.move(y, self.indent)
                s.addstr(line)
                y += 1
            s.move(self.termheight - 2, self.indent)
            s.addstr("Press any key to return to the current slide")
            s.refresh()

    def do_exec(self, cmdline):
        """
        Todo: ApiDoc

        :param cmdline:
        :return:
        """
        rc = os.system(cmdline)
        if not rc:
            # Todo: Add error message, @see: do_command_prompt
            pass

    def do_wait(self):
        """
        Todo: ApiDoc

        :return:
        """
        pass
        # Todo: seems not to be implemented yet.

    def do_begin_output(self):
        """
        Todo: ApiDoc
        Todo: Refactor with do_begin_shell_output

        :return:
        """
        with self.screen as s:
            s.move(self.cur_line, self.indent)
            s.addstr(".")
            s.addstr("-" * (self.termheight - self.indent * 2 - 2))
        self.output = True
        self.cur_line += 1

    def do_begin_shell_output(self):
        """
        Todo: ApiDoc
        Todo: Refactor with do_begin_output

        :return:
        """
        with self.screen as s:
            s.move(self.cur_line, self.indent)
            s.addstr(".")
            s.addstr("-" * (self.termheight - self.indent * 2 - 2))
        self.shelloutput = True
        self.cur_line += 1

    def do_end_output(self):
        """
        Todo: ApiDoc
        Todo: Refactor with do_end_shell_output()

        :return:
        """
        if self.output:
            with self.screen as s:
                s.move(self.cur_line, self.indent)
                s.addstr("'")
                s.addstr('-' * (self.termheight - self.indent * 2 - 2))
                s.addstr("'")
            self.output = False
            self.cur_line += 1

    def do_title(self, text):
        """
        Todo: ApiDoc

        :param text:
        :return:
        """
        self.do_bold_on()
        self.do_center(text)
        self.do_bold_off()
        self.do_center("")

    def do_footer(self, footer_text):
        """
        Todo: ApiDoc

        :param footer_text:
        :return:
        """
        self.screen.move(self.termheight - 3, (self.termwidth - len(footer_text) / 2))
        self.screen.addstr(footer_text)

    def do_header(self, header_text):
        """
        Todo: ApiDoc

        :param header_text:
        :return:
        """
        self.screen.move(1, (self.termwidth - len(header_text) / 2))
        self.screen.addstr(header_text)

    def do_author(self, author):
        """
        Todo: ApiDoc

        :param author:
        :return:
        """
        self.do_center(author)
        self.do_center('')

    def do_date(self, date):
        """
        Todo: ApiDoc

        :param date:
        :return:
        """
        self.do_center(date)
        self.do_center('')

    def do_end_shell_output(self):
        """
        Todo: ApiDoc
        Todo: Refactor with do_end_output()

        :return:
        """
        if self.shelloutput:
            with self.screen as s:
                s.move(self.cur_line, self.indent)
                s.addstr("'")
                s.addstr('-' * (self.termheight - self.indent * 2 - 2))
                s.addstr("'")
            self.shelloutput = False
            self.cur_line += 1

    def do_sleep(self, seconds):
        """
        Todo: ApiDoc

        :param seconds:
        :return:
        """
        sleep(seconds)

    def do_bold_on(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.attron(curses.A_BOLD)

    def do_bold_off(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.attroff(curses.A_BOLD)

    def do_rev_on(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.attron(curses.A_REVERSE)

    def do_rev_off(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.attroff(curses.A_REVERSE)

    def do_ul_on(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.attron(curses.A_UNDERLINE)

    def do_ul_off(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.attroff(curses.A_UNDERLINE)

    def do_begin_slide_left(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.slideoutput = True
        self.slidedir = "LEFT"

    def do_end_slide(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.slideoutput = False

    def do_begin_slide_right(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.slideoutput = True
        self.slidedir = "RIGHT"

    def do_begin_slide_top(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.slideoutput = True
        self.slidedir = "TOP"

    def do_begin_slide_bottom(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.slideoutput = True
        self.slidedir = "BOTTOM"

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

        :param text:
        :return:
        """
        width = self.termwidth - self.indent
        if self.output or self.shelloutput:
            width -= 2
        op = os.popen("figlet -f %s -w %d -k %s" % (self.figletfont, width, text), 'r')
        for line in op.readlines():
            self.print_line(line)
        op.close()

    def do_bgcolor(self, color):
        """
        Todo: ApiDoc

        :param color:
        :return:
        """
        bgcolor = ColorMap.get_color(color) or curses.COLOR_BLACK
        curses.init_pair(1, curses.COLOR_WHITE, bgcolor)
        curses.init_pair(2, curses.COLOR_YELLOW, bgcolor)
        curses.init_pair(3, curses.COLOR_RED, bgcolor)
        curses.init_pair(4, curses.COLOR_GREEN, bgcolor)
        curses.init_pair(5, curses.COLOR_BLUE, bgcolor)
        curses.init_pair(6, curses.COLOR_CYAN, bgcolor)
        curses.init_pair(7, curses.COLOR_MAGENTA, bgcolor)
        curses.init_pair(8, curses.COLOR_BLACK, bgcolor)
        if self.fgcolor:
            # Todo: how to do this in python curses?
            # curses.bkgd(curses.color_pair(self.fgcolor))
            pass
        else:
            # curses.bkgd(curses.color_pair(1))
            pass

    def do_fgcolor(self, color):
        """
        Todo: ApiDoc

        :param color:
        :return:
        """
        self.fgcolor = ColorMap.get_color_pair(color)
        self.screen.attron(curses.color_pair(self.fgcolor))

    def do_color(self, color):
        """
        Todo: ApiDoc

        :param color:
        :return:
        """
        num = ColorMap.get_color_pair(color)
        self.screen.attron(curses.color_pair(num))

    def type_line(self, line):
        """
        Todo: ApiDoc

        :param line:
        :return:
        """
        for char in line:
            self.screen.addstr(char)
            self.screen.refresh()
            r = random.randint(0, 20)
            sleep(float(5 + r) / 250)

    def slide_text(self, line):
        """
        Todo ApiDoc

        :param line:
        :return:
        """
        if line == "":
            return
        if self.slidedir == "LEFT":
            for xcount in range(len(line), 0, -1):
                with self.screen as s:
                    s.move(self.cur_line, self.indent)
                    # Todo: check python list slicing
                    # s.addstr(line[xcount .. len(line) - 1])
                    s.refresh()
                sleep(float(1) / 20)
        elif self.slidedir == "RIGHT":
            for pos in range(1, self.termwidth - self.indent):
                with self.screen as s:
                    s.move(self.cur_line, self.termwidth - pos - 1)
                    s.clrtoeol()
                    # Todo: This seems superfluous?
                    # maxpos = len(line) -1 if pos >= len(line) - 1 else pos
                    s.addstr(line[0..pos])
                    s.refresh()
                    sleep(float(1) / 20)
        elif self.slidedir == "TOP":
            new_scr = self.screen.dupwin()
            for i in range(1, self.cur_line):
                with self.screen as s:
                    # Todo: How to do this in python curses?
                    # curses.overwrite(new_scr. s)
                    s.move(i, self.indent)
                    s.addstr(line)
                    s.refresh()
                    sleep(float(1) / 20)
        elif self.slidedir == "BOTTOM":
            new_scr = self.screen.dupwin()
            for i in range(self.termheight - 1, self.cur_line, -1):
                with self.screen as s:
                    # Todo: How to do this in python curses?
                    # curses.overwrite(new_scr. s)
                    s.move(i, self.indent)
                    s.addstr(line)
                    s.refresh()
                    sleep(float(1) / 20)

    def print_line(self, line):
        """
        Todo: ApiDoc

        :param line:
        :return:
        """
        width = self.termwidth - 2 + self.indent
        if self.output or self.shelloutput:
            width -= 2
        for line in textwrap.wrap(line, width):
            with self.screen as s:
                s.move(self.cur_line, self.indent)
                if self.output or self.shelloutput:
                    s.addstr("| ")
                # Todo: How does this work in python??
                if self.shelloutput and (re.match(r'^\$', line) or re.match(r'^%', line) or re.match(r'^#', line)):
                    self.type_line(line)
                elif self.slideoutput:
                    self.slide_text(line)
                else:
                    s.addstr(line)
                if (self.output or self.shelloutput) and not self.slideoutput:
                    s.move(self.cur_line, self.termwidth - self.indent - 2)
                    s.addstr(" |")
            self.cur_line += 1

    def close(self):
        """
        Todo: ApiDoc

        :return:
        """
        curses.nocbreak()
        curses.endwin()

    def read_newpage(self, pages, current_page):
        """
        Todo: ApiDoc
        Todo: Is the second param ommittable?

        :param pages:
        :param current_page:
        :return:
        """
        page = []
        col = 0
        line = 2

        with self.screen as s:
            s.clear()
            for i in range(1, len(pages)):
                s.move(line, col * 15 + 2)
                if current_page == i:
                    s.addstr("%2d %s <=" % (i + 1, pages[i].title[0:80]))
                else:
                    s.addstr("%2d %s" % (i + 1, pages[i].title[0:80]))
                line += 1
                if line >= self.termheight - 3:
                    line = 2
                    col += 1
            prompt = "jump to slide: "
            prompt_indent = 12
            s.move(self.termheight - 2, self.indent + prompt_indent)
            s.addstr(prompt)
            # s.refresh()
            curses.echo()
            s.scan("%d" % page)
            curses.noecho()
            s.move(self.termheight - 2, self.indent + prompt_indent)
            s.addstr(" " + len(prompt) + len(str(page[0])))
            if page[0]:
                return page[0] - 1
            return - 1  # invalid page

    def store_screen(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.dupwin()

    def restore_screen(self, s):
        """
        Todo ApiDoc

        :param s:
        :return:
        """
        curses.overwrite(s, self.screen)

    def draw_slidenum(self, cur_page, max_pages, eop):
        """
        Todo: ApiDoc

        :param cur_page:
        :param max_pages:
        :param eop:
        :return:
        """
        self.screen.move(self.termheight - 2, self.indent)
        self.screen.attroff(curses.A_BOLD)  # this is bad
        self.screen.addstr("[slide #%d/%d]" % (cur_page, max_pages))
        if len(self.footer) > 0:
            self.do_footer(self.footer)
        if len(self.header) > 0:
            self.do_header(self.header)
        if eop:
            self.draw_eop_marker()

    def draw_eop_marker(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.screen.move(self.termheight - 2, self.indent -1)
        self.screen.attron(curses.A_BOLD)
        self.screen.addstr('*')
        self.screen.attroff(curses.A_BOLD)
