#!/usr/bin/python

"""
   Text Presentation Program

   Python Port from Ruby
"""

version_number = "1.3.1"
import abc
from tpp.FileParser import FileParser


def load_asciimatics():
    """
    Loads the python asciimatics module and imports its namespace into the current namespace.
    It stops the program if loading tha module fails.

    :return: void
    """
    try:
        pass
        # import modules here
    except Exception:
        print "Dependency missing: asciimatics >= 1.9"
        print "Exiting..."
        quit(1)


class TPPController(object)
    """
    Base controller all other controllers inherit from
    
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        """
        Todo: ApiDoc

        :return:
        """
        raise NotImplemented()

    @abc.abstractmethod
    def close(self):
        """
        Todo: ApiDoc

        :return:
        """
        raise NotImplemented()

    @abc.abstractmethod
    def run(self):
        """
        Todo: ApiDoc

        :return:
        """
        raise NotImplemented()


class AutoplayController(TPPController):
    """
    Implements a non interactive controller for terminal. Useful for displaying unattended presentations

    """

    def __init__(self, filename, secs, visualizer_class):
        """
        Todo: ApiDoc

        :param filename:
        :param secs:
        :param visualizer_class:
        """
        self.filename = filename
        # Todo: Check how to do this reflection thing correctly
        self.vis = visualizer_class()
        self.seconds = secs
        self.cur_page = 0
        self.reload_file = False
        self.pages = []

    def close(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.vis.close()

    def run(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.reload_file = False
        parser = FileParser(self.filename)
        self.pages = parser.get_pages()
        if self.cur_page >= len(self.pages):
            self.cur_page = len(self.pages) -1
        self.vis.clear()
        self.vis.new_page()
        self.do_run()

    def do_run(self):
        """
        Todo: ApiDoc

        :return:
        """
        while True:
            wait = False
            self.vis.draw_slidenum(self.cur_page + 1, len(self.pages), False)
            


