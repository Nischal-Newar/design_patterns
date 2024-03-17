from abc import ABCMeta, abstractmethod


class ChairInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_dimensions():
        """A static interface method"""
