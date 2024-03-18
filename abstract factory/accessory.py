from abc import ABC, abstractmethod


class Accessory(ABC):
    @abstractmethod
    def render_eyes(self) -> str:
        pass

    @abstractmethod
    def render_robe(self) -> str:
        pass

    @abstractmethod
    def render_saber(self) -> str:
        pass
