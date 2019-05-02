"""Base controller all other controllers inherit from."""
import abc


class TPPController:
    """Base controller all other controllers inherit from."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def close(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def run(self):
        """
        Todo: ApiDoc.

        :return:
        """
        raise NotImplementedError()
