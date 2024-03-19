from builder import Builder


class CastleClient(Builder):
    @staticmethod
    def construct():
        return (Builder().set_building_type("Castle").set_wall_material("Brick").set_floor("Marble").
                set_door(50).set_windows(100).get_final_product())
