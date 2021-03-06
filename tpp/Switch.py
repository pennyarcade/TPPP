"""
Emulate the look and feel of a "C-style" switch statement.

Todo: ApiDoc

This class provides the functionality we want. You only need to look at
this if you want to know how this works. It only needs to be defined
once, no need to muck around with its internals.

@see: http://code.activestate.com/recipes/410692/
"""


class Switch:
    """
    Emulate the look and feel of a "C-style" switch statement.

    Todo: ApiDoc

    This class provides the functionality we want. You only need to look at
    this if you want to know how this works. It only needs to be defined
    once, no need to muck around with its internals.

    @see: http://code.activestate.com/recipes/410692/
    """

    def __init__(self, value):
        """
        Todo: ApiDoc.

        :param value:
        """
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop."""
        yield self.match
        return StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite."""
        if self.fall or not args:
            return True
        if self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        return False
