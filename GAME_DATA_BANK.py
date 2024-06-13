
class TILE_AGILITY_EFFECTS:
    def __init__(self) -> None:
        self.DATA = { 
            "g": 0,   # Grass
            "d": 0,   # Dirt
            "w": -2,  # Water
            "m": -5   # Mountain
            }


class GRID_BATTLE_MAPS:
    def __init__(self) -> None:
        self.DATA = {
            "test_Map_0":"test_Map_0.txt"
            }


class TILE_IMAGE_FILE_PATHS:
    def __init__(self) -> None:
        self.DATA = {
            "g01": "Media/Tiles/Grass_Tile.jpg",
            "d01": "Media/Tiles/Dirt_Tile.png",
        }

class CHARACTER_IMAGE_FILE_PATHS:
    def __init__(self) -> None:
        self.DATA = {
            "P01": "Media/Sprites/test_character.png",
            "E01": "Media/Sprites/test_enemy.png",
        }