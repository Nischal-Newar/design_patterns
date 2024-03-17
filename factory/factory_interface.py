from big_chair import BigChair
from medium_chair import MediumChair
from small_chair import SmallChair


class FactoryInterface:

    @staticmethod
    def get_chair(chair):
        if chair == 'big_chair':
            return BigChair()

        if chair == 'medium_chair':
            return MediumChair()

        if chair == 'small_chair':
            return SmallChair()

        return None
