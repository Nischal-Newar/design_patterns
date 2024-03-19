class House:

    def __init__(self):
        self.floor = None
        self.windows = None
        self.door = None
        self.wall_material = None
        self.building_type = None

    def construction(self):
        return (f'Building {self.building_type} house  with {self.floor} floor design, {self.wall_material} '
                f'wall material, {self.door} doors and {self.windows} windows.')
