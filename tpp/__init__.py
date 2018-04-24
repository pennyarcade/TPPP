#!/usr/bin/python
"""
Text Presentation Program

Python Port from Ruby

To roll out TPP as a package this becomes the main file to run
"""
import tpp.controller
import tpp.visualizer

from tpp.ColorMap import ColorMap
from tpp.FileParser import FileParser
from tpp.Page import Page
from tpp.Switch import Switch
from tpp.TPPRunner import TPPRunner


if __name__ == "__main__":
    RUNNER = TPPRunner()
    RUNNER.run()
