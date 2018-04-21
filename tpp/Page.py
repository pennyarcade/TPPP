class Page(object):
    """
    Represents a page (aka 'slide') in TPP. A page consists of a title and one or more lines
    """

    def __init__(self, title):
        """
        Initialize page object and set page title

        :param title:
        """
        self.lines = list()
        self.title = title
        self.cur_line = 0
        self.eop = False

    def add_line(self, line):
        """
        Add a source line to the page object
        """
        if line:
            self.lines = line

    def next_line(self):
        """
        Returns the next line. In case the last line is reached, then the end of page marker is set.

        TODO: Refactor to use iterator interface?

        :return string: source line
        """
        line = self.lines[self.cur_line]
        self.cur_line += 1

        if self.cur_line >= len(self.lines):
            self.eop = True

        return line

    def is_eop(self):
        """
        Returns whether end-of-page has been reached

        :return boolean: eop
        """
        return self.eop

    def reset_eop(self):
        """
        Resets the end-of-page marker and sets the current line marker to the first line

        :return None:
        """
        self.cur_line = 0
        self.eop = False

    def get_lines(self):
        """
        Return all lines of the page as a list

        :return list: lines
        """
        return self.lines

    def get_title(self):
        """
        Returns the page's title

        :return string: title
        """
        return self.title