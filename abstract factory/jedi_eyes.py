from accessory import Accessory


class JediAccessories(Accessory):

    def render_eyes(self) -> str:
        return "Blue"

    def render_robe(self) -> str:
        return "White"

    def render_saber(self) -> str:
        return "Blue"
