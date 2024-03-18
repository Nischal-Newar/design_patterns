from abc import ABC, abstractmethod


class AbstractClassFactory(ABC):

    @abstractmethod
    def render(self) -> dict:
        pass
