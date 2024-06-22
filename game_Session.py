import pygame
import map_Display
import map_Data
import GAME_DATA_BANK
import os
import time

GRID_BATTLE_MAPS = GAME_DATA_BANK.GRID_BATTLE_MAP_FILE_PATHS().DATA
GRID_BATTLE_CHARACTERS = GAME_DATA_BANK.GRID_BATTLE_CHARACTER_FILE_PATHS().DATA


class Game:
    def __init__(self):
        """
        Initialize the game, setting up the window, clock, and game elements.
        """
        
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Placeholder Game Name")

        # Get the current screen resolution
        self.screen_info = pygame.display.Info()
        self.screen_width = self.screen_info.current_w
        self.screen_height = self.screen_info.current_h

        # Calculate 80% of the screen resolution
        self.window_width = int(self.screen_width * 0.6)
        self.window_height = int(self.screen_height * 0.6)

        self.surface = pygame.display.set_mode((self.window_width, self.window_height))
        self.BG_COLOR = ("black")
        self.running = True
        

        loaded_grid_tile_info, loaded_player_characters, loaded_enemy_characters  = self.load_scenario("TEST_MAP_000","TEST_PLAYER_000","TEST_ENEMY_000")
        

        self.battle_grid = map_Data.Battle_Grid(loaded_grid_tile_info, loaded_player_characters, loaded_enemy_characters)
        self.board_dimensions = [len(loaded_grid_tile_info),len(loaded_grid_tile_info[0])]

        # Calculate the dynamic tile size
        # minimum of the height and breadth because the tiles will always be square and could thus not fit into the screen
        self.tile_size = min(self.window_width // self.battle_grid.dimensions[0], self.window_height // self.battle_grid.dimensions[1])

        self.tiles = map_Display.Tiles(self.surface, self.battle_grid.grid_tile_info, self.tile_size, self.window_width, self.window_height)
        self.characters = map_Display.Characters_Display(self.surface, self.battle_grid.grid_tile_info, self.tile_size, self.window_width, self.window_height)
        self.tile_coordinates = self.tiles.get_tile_coordinate_ranges()
    
    def load_scenario(self, map_id, players_id, enemy_id):
        """
        Load map data from a text file and populate self.map_data.
        """


        map_path = os.path.join("Maps", GRID_BATTLE_MAPS[map_id]) 
        player_path = os.path.join("Characters", GRID_BATTLE_CHARACTERS[players_id]) 
        enemy_path = os.path.join("Characters", GRID_BATTLE_CHARACTERS[enemy_id]) 
        
        grid_tile_info = []
        filepath = os.path.join(map_path)

        try:
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        # Split line into parts separated by ";", strip each part of whitespace
                        temp_list = [part.strip() for part in line.split(";") if part.strip()]
                        grid_tile_info.append(temp_list)
        except FileNotFoundError:
            print(f"Error: Map file not found at {filepath}")
            # Optionally, handle the error (e.g., load default map or exit game)

        player_characters = {}
        filepath = os.path.join(player_path)
        try:
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        # Split line into parts separated by ";", strip each part of whitespace
                        temp_list = [part.strip() for part in line.split(";") if part.strip()]
                        player_characters[temp_list[3]] = map_Data.Character(temp_list[0].split(","),temp_list[1],temp_list[2],temp_list[3],int(temp_list[4]),int(temp_list[5]),int(temp_list[6]),int(temp_list[7]),int(temp_list[8]),int(temp_list[9]),temp_list[10].split(","),temp_list[11].split(","))
        except FileNotFoundError:
            print(f"Error: Map file not found at {filepath}")
            # Optionally, handle the error (e.g., load default map or exit game)




        enemy_characters = {}
        filepath = os.path.join(enemy_path)
        try:
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        # Split line into parts separated by ";", strip each part of whitespace
                        temp_list = [part.strip() for part in line.split(";") if part.strip()]
                        enemy_characters[temp_list[3]] = map_Data.Character(temp_list[0].split(","),temp_list[1],temp_list[2],temp_list[3],int(temp_list[4]),int(temp_list[5]),int(temp_list[6]),int(temp_list[7]),int(temp_list[8]),int(temp_list[9]),temp_list[10].split(","),temp_list[11].split(","))
        except FileNotFoundError:
            print(f"Error: Map file not found at {filepath}")
            # Optionally, handle the error (e.g., load default map or exit game)

        #Populate board with characters
        player_ids = list(player_characters.keys())
        enemy_ids = list(enemy_characters.keys())
        

        player_index = 0
        enemy_index = 0

        for i in range(len(grid_tile_info)):
            for j in range(len(grid_tile_info[0])):
                if grid_tile_info[i][j][4:6] == "EA": 
                    old_tile_info = grid_tile_info[i][j][:4]
                    grid_tile_info[i][j] = old_tile_info + enemy_characters[enemy_ids[enemy_index]].image_id + enemy_ids[enemy_index]
                    enemy_index += 1
                    
                elif grid_tile_info[i][j][4:6] == "PA":
                    old_tile_info = grid_tile_info[i][j][:4]
                    grid_tile_info[i][j] = old_tile_info + player_characters[player_ids[player_index]].image_id + player_ids[player_index]
                    player_index += 1
        
        print(grid_tile_info)
        return grid_tile_info, player_characters,enemy_characters

    def events(self):
        """
        Handle user input and events like quitting the game or pressing the escape key.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        x, y = event.pos
                        self.handle_left_click(x, y)
                    elif event.button == 3:  # Right mouse button
                        x, y = event.pos
                        self.handle_right_click(x, y)

    def handle_left_click(self, x, y):
        """
        Handle left mouse button click.
        
        :param x: X coordinate of the mouse click.
        :param y: Y coordinate of the mouse click.
        """
        tile_coords = [None,None]
    
        for i in range(self.battle_grid.dimensions[0]):
            for j in range(self.battle_grid.dimensions[1]):
                if x >= self.tile_coordinates[i][j][0][0] and x <= self.tile_coordinates[i][j][1][0] and y >= self.tile_coordinates[i][j][0][1] and y <= self.tile_coordinates[i][j][1][1]:
                    tile_coords = [i,j]
                    break

        if tile_coords[0] == None or tile_coords[1] == None:
            print(f"ERROR: No tile present at these coordinates")

        elif self.battle_grid.updating_character_position:
            print(f"ERROR: Currently updating character position")
        else: 

            if not self.battle_grid.tile_selected:
                self.battle_grid.select_tile_attempt(tile_coords)
                if self.battle_grid.tile_selected:
                    print(f"Left click: Valid tile selected [Row: {tile_coords[0]}, Column: {tile_coords[1]}]\n")
                else:
                    print(f"Left click: invalid tile selected [Row: {tile_coords[0]}, Column: {tile_coords[1]}]\n")
                
            else:
                self.battle_grid.selected_tile_move_attempt(tile_coords)
                print(f"Left click: tile selected and move made to [Row: {tile_coords[0]}, Column: {tile_coords[1]}]\n")
                
                
            

    def handle_right_click(self, x, y):
        """
        Handle right mouse button click.
        
        :param x: X coordinate of the mouse click.
        :param y: Y coordinate of the mouse click.
        """
        
        print(f"Right click at pixel coordinates ({x}, {y})")

    def update(self):
        """
        Update the game state.
        """
        if self.battle_grid.updating_character_position:
            self.battle_grid.update_character_position(self.battle_grid.next_character_move[2][self.battle_grid.character_movement_index])
            self.battle_grid.character_movement_index += 1

            if self.battle_grid.character_movement_index >=  self.battle_grid.character_movements_total:
                self.battle_grid.updating_character_position = False

            time.sleep(0.5)

        self.tiles.load_data(self.battle_grid.grid_tile_info)
        self.tiles.calculate_offset()
        self.characters.load_data(self.battle_grid.grid_tile_info)
        self.characters.calculate_offset()
        self.tile_coordinates = self.tiles.get_tile_coordinate_ranges()
        return


    def draw(self):
        """
        Clear the screen, draw tiles and characters, and update the display.
        """
        self.surface.fill(self.BG_COLOR)
        self.tiles.draw(self.surface)
        self.characters.draw()
        pygame.display.update()

    def start_game_session(self):
        """
        Main game loop that handles events, updates, and drawing.
        """
        while self.running:
            self.events()
            self.update()
            self.draw()
            

if __name__ == "__main__":
    mygame = Game()
    mygame.start_game_session()