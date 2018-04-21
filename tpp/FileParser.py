from tpp import Page


class FileParser(object):
    """
    Opens a TPP source file and returns a list of page objects
    """

    def __init__(self, filename):
        """
        Initialize source parser

        :param filename:
        """
        self.file = None
        self.file_name = filename
        self.pages = list()
        self.page_number = 0

    def get_pages(self):
        """
        Parses the specified file ane returns a list of page objects

        :return list:
        """
        try:
            self.file = open(self.file_name, "r")
        except IOError:
            print "Could not open source file: " + self.file_name
            print "Exiting..."
            quit(1)

        cur_page = Page("slide " + str(self.page_number + 1))

        for line in self.file:
            line = line.strip()

            if line.startswith('--##'):
                pass
                # ignore comments
            elif line.startswith('--newpage'):
                self.pages.append(cur_page)
                self.page_number += 1
                name = line.replace("--newpage", '').strip()
                if name == "":
                    name = "slide " + str(self.page_number + 1)

                cur_page = Page(name)
            else:
                cur_page.add_line(line)

        self.pages.append(cur_page)