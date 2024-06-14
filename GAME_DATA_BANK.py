
class TILE_AGILITY_EFFECTS:
    def __init__(self) -> None:
        self.DATA = { 
            "g": 0,   # Grass
            "d": 0,   # Dirt
            "w": -2,  # Water
            "m": -5   # Mountain
            }


class GRID_BATTLE_MAP_FILE_PATHS:
    def __init__(self) -> None:
        self.DATA = {
            "TEST_MAP_000":"test_Map_0.txt"
            }

class GRID_BATTLE_CHARACTER_FILE_PATHS:
    def __init__(self) -> None:
        self.DATA = {
            "TEST_PLAYER_000":"player_characters_000.txt",
            "TEST_ENEMY_000":"enemy_characters_000.txt",
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


class CHARACTER_STATUSES:
    def __init__(self) -> None:
        self.DATA = {
            # (current_HP, max_HP, ATK, SHIELD, AGI)
            "POISONED": [3,(-1,0,0,0,0)],
            "BLEEDING": [3,(-1,0,0,0,0)]
            
        }      

class CHARACTER_EQUIPMENT:
    def __init__(self) -> None:
        self.DATA = {
            # (current_HP, max_HP, ATK, SHIELD, AGI)
            "SMALL_SHIELD": (0,0,0,1,0),
            "MEDIUM_SHIELD": (0,0,0,2,0),
            "LARGE_SHIELD": (0,0,0,3,-1),
        }     


