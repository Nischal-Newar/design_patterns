from chair_interface import ChairInterface


class MediumChair(ChairInterface):
    def __init__(self):
        self._height = 10
        self._width = 10
        self._length = 10

    def get_dimensions(self):
        return {
            "width": self._width,
            "height": self._height,
            "length": self._length
        }
