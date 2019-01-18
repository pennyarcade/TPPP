"""Implements a generic visualizer from which all other visualizers need to be derived."""

import abc
import textwrap


class TPPVisualizer:
    """Implements a generic visualizer from which all other visualizers need to be derived."""

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Initialize basic visualizer."""
        self.footer = ''
        self.header = ''

    @staticmethod
    def split_lines(text, width=70):
        """
        Splits a line of text into several lines.

        Where each of the result lines is at most _width_ characters long,
        caring about word boundaries, and returns an array of strings.

        Todo: set sensible textwrap parameters? All default for now.

        :param text:
        :param width:
        :return:
        """
        return textwrap.wrap(text, width)

    @abc.abstractmethod
    def do_footer(self, footer_text):
        """
        Todo: ApiDoc.

        :param footer_text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_header(self, header_text):
        """
        Todo: ApiDoc.

        :param header_text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_refresh(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def new_page(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_heading(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_with_border(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_hor_line(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_color(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_center(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_right(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_exec(self, cmdline):
        """
        Todo: ApiDoc.

        :param cmdline:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_wait(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_begin_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_begin_shell_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_end_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_end_shell_output(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_sleep(self, seconds):
        """
        Todo: ApiDoc.

        :param seconds: Time to sleep
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_bold_on(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_bold_off(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_rev_on(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_rev_off(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_ul_on(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_ul_off(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_begin_slide_left(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_end_slide(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_command_prompt(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_begin_slide_right(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_begin_slide_top(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_begin_slide_bottom(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_set_huge_font(self, params):
        """
        Todo: ApiDoc.

        :param params: list of parameters
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_huge(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def print_line(self, text: str):
        """
        Todo: ApiDoc.

        :param text: str
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_title(self, text):
        """
        Todo: ApiDoc.

        :param text:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_author(self, text: str):
        """
        Todo: ApiDoc.

        :param text: str
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_date(self, text: str):
        """
        Todo: ApiDoc.

        :param text: str
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_bg_color(self, color):
        """
        Todo: ApiDoc.

        :param color:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_fg_color(self, color):
        """
        Todo: ApiDoc.

        :param color:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def do_color(self, color):
        """
        Todo: ApiDoc.

        :param color:
        :return:
        """
        raise NotImplementedError()

    def visualize(self, line, eop):
        """
        Receives a _line_, parses if id necessary, and dispatches it to the correct method.

        Which then does the correct processing. It returns whether the controller shall wait for input.

        Todo: Refactor this to use reflection to find the right method

        :param line:
        :param eop:
        :return boolean: wait for input
        """
        if line.startswith('--heading'):
            return self.do_heading(line.replace('--heading', '').strip())
        if line.startswith('--withborder'):
            return self.do_with_border()
        if line.startswith('--horline'):
            return self.do_hor_line()
        if line.startswith('--color'):
            return self.do_color(line.replace('--color', '').strip())
        if line.startswith('--center'):
            return self.do_center(line.replace('--center', '').strip())
        if line.startswith('--right'):
            return self.do_right(line.replace('--right', '').strip())
        if line.startswith('--exec'):
            return self.do_exec(line.replace('--exec', '').strip())
        if line.startswith('---'):
            return self.do_wait()
        if line.startswith('--beginoutput'):
            return self.do_begin_output()
        if line.startswith('--beginshelloutput'):
            return self.do_begin_shell_output()
        if line.startswith('--endoutput'):
            return self.do_end_output()
        if line.startswith('--endshelloutput'):
            return self.do_end_shell_output()
        if line.startswith('--sleep'):
            return self.do_sleep(line.replace('--sleep', '').strip())
        if line.startswith('--boldon'):
            return self.do_bold_on()
        if line.startswith('--boldoff'):
            return self.do_bold_off()
        if line.startswith('--revon'):
            return self.do_rev_on()
        if line.startswith('--revoff'):
            return self.do_rev_off()
        if line.startswith('--ulon'):
            return self.do_ul_on()
        if line.startswith('--uloff'):
            return self.do_ul_off()
        if line.startswith('--beginslideleft'):
            return self.do_begin_slide_left()
        if line.startswith('--endslideleft'):
            return self.do_end_slide()
        if line.startswith('--endslideright'):
            return self.do_end_slide()
        if line.startswith('--endslidetop'):
            return self.do_end_slide()
        if line.startswith('--endslidebottom'):
            return self.do_end_slide()
        if line.startswith('--beginslideright'):
            return self.do_begin_slide_right()
        if line.startswith('--beginslidetop'):
            return self.do_begin_slide_top()
        if line.startswith('--beginslidebottom'):
            return self.do_begin_slide_bottom()
        if line.startswith('--sethugefont'):
            return self.do_set_huge_font(line.replace('--sethugefont', '').strip())
        if line.startswith('--huge'):
            return self.do_huge(line.replace('--huge', '').strip())
        if line.startswith('--footer'):
            text = line.replace('--footer', '').strip()
            if text != "":
                self.footer = text
            return self.do_footer(self.footer)
        if line.startswith('--header'):
            text = line.replace('--header', '').strip()
            if text != "":
                self.header = text
            return self.do_header(self.header)
        if line.startswith('--title'):
            return self.do_title(line.replace('--title', '').strip())
        if line.startswith('--author'):
            return self.do_author(line.replace('--author', '').strip())
        if line.startswith('--sleep'):
            return self.do_sleep(line.replace('--sleep', '').strip())
        if line.startswith('--date'):
            return self.do_date(line.replace('--date', '').strip())
        if line.startswith('--bgcolor'):
            return self.do_bg_color(line.replace('--bgcolor', '').strip())
        if line.startswith('--fgcolor'):
            return self.do_fg_color(line.replace('--fgcolor', '').strip())
        if line.startswith('--color'):
            return self.do_color(line.replace('--color', '').strip())
        return self.print_line(line.strip())

    def close(self):
        """
        Todo: ApiDoc.

        Todo: Where is this used?

        :return None:
        """
        pass
        # do nothing, really?
