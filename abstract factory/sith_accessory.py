from accessory import Accessory


class SithAccessories(Accessory):

    def render_eyes(self) -> str:
        return "Red"

    def render_robe(self) -> str:
        return "Black"

    def render_saber(self) -> str:
        return "Red"
