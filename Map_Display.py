import pygame
import os

# Constants for the game
#title = "grid_map"
#tiles_horizontal = 8
#tiles_vertical = 8
#tilesize = 64

# Window dimensions
#window_width = tilesize * tiles_horizontal
#window_height = tilesize * tiles_vertical

class Tile:
    def __init__(self, id, x, y, tile_type,tile_size):
        """
        Initialize a tile.

        :param id: Unique identifier for the tile.
        :param x: X coordinate of the tile in the grid.
        :param y: Y coordinate of the tile in the grid.
        :param tile_type: Type of the tile, which determines its image.
        """
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.tile_type = tile_type
        self.tile_size = tile_size

        # Dictionary to map tile types to image file paths
        tile_images = {
            "g01": "Media/Tiles/Grass_Tile.jpg",
            "d01": "Media/Tiles/Dirt_Tile.png",
        }

        # Load the appropriate image based on the tile type
        if tile_type in tile_images:
            filepath = tile_images[tile_type]
        else:
            raise ValueError(f"Error: Tile Type {tile_type}")

        self.rect = pygame.Rect(self.x * self.tile_size, self.y * self.tile_size, self.tile_size, self.tile_size)
        self.image = pygame.image.load(filepath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))

    def set_offset(self, offset_x, offset_y):
        """
        Set the offset for the tile.

        :param offset_x: Offset in the x direction.
        :param offset_y: Offset in the y direction.
        """
        self.rect.x += offset_x
        self.rect.y += offset_y

    def debug_print(self):
        """
        Print the tile's details for debugging purposes.
        """
        s = "id: {}, x: {}, y: {}, kind: {}".format(self.id, self.x, self.y, self.tile_type)
        print(s)

class Tiles:
    def __init__(self, screen, board_dimensions, tile_size, window_width, window_height):
        """
        Initialize the Tiles manager.

        :param screen: Pygame surface to draw tiles on.
        """
        self.tiles_horizontal = board_dimensions[0]
        self.tiles_vertical = board_dimensions[1]
        self.tile_size = tile_size
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen
        self.inner = []
        self.load_data()
        self.calculate_offset()
        
        


    def load_data(self):
        """
        Load the tile data from a file and initialize Tile objects.
        """
        self.inner = []
        filepath = os.path.join("Maps", "Tile_Map_Test.txt")
        with open(filepath, "r") as f:
            mylines = f.readlines()
            mylines = [i.strip() for i in mylines if len(i.strip()) > 0]

        id = 0
        for count_i, myline in enumerate(mylines):
            temp_list = myline.split(";")
            temp_list = [i.strip() for i in temp_list if len(i.strip()) > 0]

            for count_j, elem in enumerate(temp_list):
                tile_type = elem.split("_")[0]
                new_tile = Tile(id, count_j, count_i, tile_type, self.tile_size)
                self.inner.append(new_tile)
                id += 1

    def calculate_offset(self):
        """
        Calculate the offset to center the map on the screen.
        """
        map_width = self.tiles_horizontal * self.tile_size
        map_height = self.tiles_vertical * self.tile_size
        offset_x = (self.window_width - map_width) // 2
        offset_y = (self.window_height - map_height) // 2

        for tile in self.inner:
            tile.set_offset(offset_x, offset_y)

    def draw(self, surface):
        """
        Draw all tiles onto the provided surface.

        :param surface: Pygame surface to draw tiles on.
        """
        if len(self.inner) == 0:
            raise ValueError("No Tiles to load in")
        for elem in self.inner:
            surface.blit(elem.image, elem.rect)

    def debug_print(self):
        """
        Print details of all tiles for debugging purposes.
        """
        for elem in self.inner:
            elem.debug_print()

class Character_Display:
    def __init__(self, id, x, y, character_kind, tile_size):
        """
        Initialize a character.

        :param id: Unique identifier for the character.
        :param x: X coordinate of the character in the grid.
        :param y: Y coordinate of the character in the grid.
        :param character_kind: Type of the character, which determines its image.
        """
        self.id = id
        self.x, self.y = int(x), int(y)
        self.myinc = 0.5
        self.tile_size = tile_size

        # Dictionary to map character types to image file paths
        character_images = {
            "P01": "Media/Sprites/test_character.png",
            "E01": "Media/Sprites/test_enemy.png",
        }

        # Load the appropriate image based on the character kind
        if character_kind in character_images:
            self.character_image = character_images[character_kind]
        else:
            raise ValueError(f"Sorry, do not recognize that: {character_kind}")

        self.image = pygame.image.load(self.character_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))

        # Initialize the rect attribute
        self.rect = pygame.Rect(self.x * self.tile_size, self.y * self.tile_size, self.tile_size, self.tile_size)

    def set_offset(self, offset_x, offset_y):
        """
        Set the offset for the character.

        :param offset_x: Offset in the x direction.
        :param offset_y: Offset in the y direction.
        """
        self.rect.x += offset_x
        self.rect.y += offset_y

    def debug_print(self):
        """
        Print the character's details for debugging purposes.
        """
        s = "id: {}, x: {}, y: {}".format(self.id, self.rect.x, self.rect.y)
        print(s)

class Characters_Display:
    def __init__(self, surface, board_dimensions, tile_size, window_width, window_height):
        """
        Initialize the Characters_Display manager.

        :param surface: Pygame surface to draw characters on.
        """
        self.surface = surface
        self.inner = []
        self.tile_size = tile_size
        self.tiles_horizontal = board_dimensions[0]
        self.tiles_vertical = board_dimensions[1]
        self.window_width = window_width
        self.window_height = window_height
        self.load_data()
        self.calculate_offset()

    def load_data(self):
        """
        Load the character data from a file and initialize Character_Display objects.
        """
        filepath = os.path.join("Maps", "Tile_Map_Test.txt")
        with open(filepath, "r") as f:
            mylines = f.readlines()
            mylines = [i.strip() for i in mylines if len(i.strip()) > 0]

        id = 0
        for count_i, line in enumerate(mylines):
            temp_list = line.split(";")
            for count_j, elem in enumerate(temp_list):
                if len(elem.split("_")) > 1 and elem.split("_")[1] in ["P01", "E01"]:
                    character_kind = elem.split("_")[1]
                    new_character = Character_Display(id, count_j, count_i, character_kind, self.tile_size)
                    self.inner.append(new_character)
                    id += 1

    def calculate_offset(self):
        """
        Calculate the offset to center the characters on the screen.
        """
        map_width = self.tiles_horizontal * self.tile_size
        map_height = self.tiles_vertical * self.tile_size
        offset_x = (self.window_width - map_width) // 2
        offset_y = (self.window_height - map_height) // 2

        for character in self.inner:
            character.set_offset(offset_x, offset_y)

    def draw(self):
        """
        Draw all characters onto the provided surface.
        """
        if len(self.inner) == 0:
            raise ValueError("No characters to display")
        for elem in self.inner:
            self.surface.blit(elem.image, elem.rect)

    def debug_print(self):
        """
        Print details of all characters for debugging purposes.
        """
        for elem in self.inner:
            elem.debug_print()
