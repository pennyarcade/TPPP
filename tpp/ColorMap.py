class ColorMap(object):
    """
    maps color names to constants and indexes
    """
    colors = {
        "black":   "COLOUR_BLACK",
        "red":     "COLOUR_RED",
        "green":   "COLOUR_GREEN",
        "yellow":  "COLOUR_YELLOW",
        "blue":    "COLOUR_BLUE",
        "magenta": "COLOUR_MAGENTA",
        "cyan":    "COLOUR_CYAN",
        "white":   "COLOUR_WHITE",
        "default": -1
    }

    color_pairs = {
        "black": 8,
        "red": 3,
        "green": 4,
        "yellow": 2,
        "blue": 5,
        "magenta": 7,
        "cyan": 6,
        "white": 1,
        "default": -1
    }

    def get_color(self, color):
        """
        Maps color name _color_ to a constant

        :param color:
        :return int:
        """
        return self.colors[color]

    def get_color_pair(self, color):
        """
        Maps color name to a color pair index

        :param color:
        :return int:
        """
        return self.color_pairs[color]