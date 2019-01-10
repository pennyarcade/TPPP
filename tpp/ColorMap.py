"""
Maps color names to constants and indexes.
"""
import curses


class ColorMap:
    """
    Maps color names to constants and indexes.
    """
    colors = {
        "black":   curses.COLOR_BLACK,
        "red":     curses.COLOR_RED,
        "green":   curses.COLOR_GREEN,
        "yellow":  curses.COLOR_YELLOW,
        "blue":    curses.COLOR_BLUE,
        "magenta": curses.COLOR_MAGENTA,
        "cyan":    curses.COLOR_CYAN,
        "white":   curses.COLOR_WHITE,
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

    def get_color(color: int):
        """
        Maps color name _color_ to a constant

        :param color: int
        :return int:
        """
        return ColorMap.colors[color]

    def get_color_pair(color: str):
        """
        Maps color name to a color pair index

        :param color: str
        :return int:
        """
        return ColorMap.color_pairs[color]
