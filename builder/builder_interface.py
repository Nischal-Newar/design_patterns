from abc import ABC, abstractmethod


class BuilderInterface(ABC):

    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        """Build Type"""

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        """Wall Material Type"""

    @staticmethod
    @abstractmethod
    def set_door(door_count):
        """Door Count"""

    @staticmethod
    @abstractmethod
    def set_floor(floor_type):
        """Floor Type"""

    @staticmethod
    @abstractmethod
    def set_windows(windows_count):
        """Windows Count"""

    @staticmethod
    @abstractmethod
    def get_final_product():
        """Return Final Product"""
