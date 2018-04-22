"""
Implements a non interactive controller to controt non-interactive visualizers

(i.e. those that are used for converting TPP souce code into another format)
"""
from time import sleep

from tpp.FileParser import FileParser
from tpp.controller.TPPController import TPPController


class ConversionController(TPPController):
    """
    Implements a non interactive controller to controt non-interactive visualizers

    (i.e. those that are used for converting TPP souce code into another format)
    """
    def __init__(self, input, output, visualizer_class):
        """
        Todo: ApiDoc

        :param input:
        :param output:
        :param visualizer_class:
        """
        parser = FileParser(input)
        self.pages = parser.get_pages()
        self.vis = visualizer_class(output)

    def run(self):
        """
        Todo: ApiDoc

        :return:
        """
        for page in self.pages:
            while True:
                eop = page.is_eop()
                self.vis.visualize(page.next_line(), eop)
                if eop:
                    break

    def close(self):
        """
        Todo: ApiDoc

        :return:
        """
        self.vis.close()
