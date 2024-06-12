import pygame
import os

title = "grid_map"
tiles_horizontal = 8
tiles_vertical = 8
tilesize = 64

window_width = tilesize * tiles_horizontal
window_height = tilesize * tiles_vertical

class Tile:
    def __init__(self, id, x, y, tile_type):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.tile_type = tile_type

        tile_images = {
            "g01": "Media/Tiles/Grass_Tile.jpg",
            "d01": "Media/Tiles/Dirt_Tile.png",
        }

        if tile_type in tile_images:
            filepath = tile_images[tile_type]
        else:
            raise ValueError(f"Error: Tile Type {tile_type}")

        self.rect = pygame.Rect(self.x * tilesize, self.y * tilesize, tilesize, tilesize)
        self.image = pygame.image.load(filepath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tilesize, tilesize))

    def set_offset(self, offset_x, offset_y):
        self.rect.x += offset_x
        self.rect.y += offset_y

    def debug_print(self):
        s = "id: {}, x: {}, y: {}, kind: {}"
        s = s.format(self.id, self.x, self.y, self.tile_type)
        print(s)

class Tiles:
    def __init__(self, screen):
        self.screen = screen
        self.inner = []
        self.load_data()
        self.calculate_offset()

    def load_data(self):
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
                new_tile = Tile(id, count_j, count_i, tile_type)
                self.inner.append(new_tile)
                id += 1

    def calculate_offset(self):
        map_width = tiles_horizontal * tilesize
        map_height = tiles_vertical * tilesize
        offset_x = (window_width - map_width) // 2
        offset_y = (window_height - map_height) // 2

        for tile in self.inner:
            tile.set_offset(offset_x, offset_y)

    def draw(self, surface):
        if len(self.inner) == 0:
            raise ValueError("No Tiles to load in")
        for elem in self.inner:
            surface.blit(elem.image, elem.rect)

    def debug_print(self):
        for elem in self.inner:
            elem.debug_print()

class Character_Display:
    def __init__(self, id, x, y, character_kind):
        self.id = id
        self.x, self.y = int(x), int(y)
        self.myinc = 0.5

        character_images = {
            "P01": "Media/Sprites/test_character.png",
            "E01": "Media/Sprites/test_enemy.png",
        }

        if character_kind in character_images:
            self.character_image = character_images[character_kind]
        else:
            raise ValueError(f"Sorry, do not recognize that: {character_kind}")

        self.image = pygame.image.load(self.character_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tilesize, tilesize))

        # Initialize the rect attribute
        self.rect = pygame.Rect(self.x * tilesize, self.y * tilesize, tilesize, tilesize)

    def set_offset(self, offset_x, offset_y):
        self.rect.x += offset_x
        self.rect.y += offset_y

    def debug_print(self):
        s = "id: {}, x: {}, y: {}".format(self.id, self.rect.x, self.rect.y)
        print(s)

class Characters_Display:
    def __init__(self, surface):
        self.surface = surface
        self.inner = []
        self.load_data()
        self.calculate_offset()

    def load_data(self):
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
                    new_character = Character_Display(id, count_j, count_i, character_kind)
                    self.inner.append(new_character)
                    id += 1

    def calculate_offset(self):
        map_width = tiles_horizontal * tilesize
        map_height = tiles_vertical * tilesize
        offset_x = (window_width - map_width) // 2
        offset_y = (window_height - map_height) // 2

        for character in self.inner:
            character.set_offset(offset_x, offset_y)

    def draw(self):
        if len(self.inner) == 0:
            raise ValueError("No characters to display")
        for elem in self.inner:
            self.surface.blit(elem.image, elem.rect)

    def debug_print(self):
        for elem in self.inner:
            elem.debug_print()
