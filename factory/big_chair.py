from chair_interface import ChairInterface


class BigChair(ChairInterface):
    def __init__(self):
        self._height = 15
        self._width = 15
        self._length = 15

    def get_dimensions(self):
        return {
            "width": self._width,
            "height": self._height,
            "length": self._length
        }
