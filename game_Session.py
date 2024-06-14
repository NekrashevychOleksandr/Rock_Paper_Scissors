import pygame
import map_Display
import map_Data
import os


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
        

        loaded_grid_tile_info = self.load_map()
        

        player_characters = {}
        enemy_characters = {}

        for tile_row in loaded_grid_tile_info:
            for tile in tile_row:
                if tile[4] == "E": 
                    enemy_characters[tile[7:10]] = map_Data.Character([], "Test Name", tile[7:10], 1, 5, 5, 1, 0, 1, [], [])
                elif tile[4] == "P":
                    player_characters[tile[7:10]] = map_Data.Character([], "Test Name", tile[7:10], 1, 5, 5, 1, 0, 1, [], [])

        

        self.battle_grid = map_Data.Battle_Grid(loaded_grid_tile_info, player_characters, enemy_characters)
        self.board_dimensions = [len(loaded_grid_tile_info),len(loaded_grid_tile_info[0])]

        # Calculate the dynamic tile size
        # minimum of the height and breadth because the tiles will always be square and could thus not fit into the screen
        self.tile_size = min(self.window_width // self.battle_grid.dimensions[0], self.window_height // self.battle_grid.dimensions[1])

        self.tiles = map_Display.Tiles(self.surface, self.battle_grid.grid_tile_info, self.tile_size, self.window_width, self.window_height)
        self.characters = map_Display.Characters_Display(self.surface, self.battle_grid.grid_tile_info, self.tile_size, self.window_width, self.window_height)
        self.tile_coordinates = self.tiles.get_tile_coordinate_ranges()
    
    def load_map(self):
        """
        Load map data from a text file and populate self.map_data.
        """
        current_map = "test_Map_0.txt" # later we can add in the map list
        map_data = []
        filepath = os.path.join("Maps",current_map)  # Adjust path as per your file structure

        try:
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        # Split line into parts separated by ";", strip each part of whitespace
                        temp_list = [part.strip() for part in line.split(";") if part.strip()]
                        map_data.append(temp_list)
        except FileNotFoundError:
            print(f"Error: Map file not found at {filepath}")
            # Optionally, handle the error (e.g., load default map or exit game)

        # Print loaded map data for debugging
        print("Loaded map data:")
        for row in map_data:
            print(row)

        return map_data

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