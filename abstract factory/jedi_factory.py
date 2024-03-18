from jedi_eyes import JediAccessories
from abstract_class_factory import AbstractClassFactory

class JediFactory(AbstractClassFactory):

    def render(self) -> dict:
        return {
            "robe": JediAccessories.render_saber(),
            "eyes": JediAccessories.render_eyes(),
        }
