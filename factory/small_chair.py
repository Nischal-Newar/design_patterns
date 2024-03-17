from chair_interface import ChairInterface


class SmallChair(ChairInterface):
    def __init__(self):
        self._height = 5
        self._width = 5
        self._length = 5

    def get_dimensions(self):
        return {
            "width": self._width,
            "height": self._height,
            "length": self._length
        }
