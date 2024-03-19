from house import House
from builder_interface import BuilderInterface


class Builder(BuilderInterface):

    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def set_windows(self, windows_count):
        self.house.windows = windows_count
        return self

    def set_door(self, door_count):
        self.house.door = door_count
        return self

    def set_floor(self, floor_type):
        self.house.floor = floor_type
        return self

    def get_final_product(self):
        return self.house
