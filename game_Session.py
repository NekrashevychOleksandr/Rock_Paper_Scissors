import pygame
import map_Display
import map_Data


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
        self.window_width = int(self.screen_width * 0.8)
        self.window_height = int(self.screen_height * 0.8)

        self.surface = pygame.display.set_mode((self.window_width, self.window_height))
        self.BG_COLOR = ("black")
        self.running = True

        # Default board dimensions will be pulled from a file later
        self.board_dimensions = [8,8]



        loaded_grid_tile_info = [["g01*___","g01*P01","g01*___","g01*___","d01*___","d01*___","g01*___","g01*P01"],
                          ["g01*___","g01*___","g01*___","g01*___","d01*P01","d01*___","g01*___","g01*___"],
                          ["g01*___","d01*___","g01*P01","g01*___","d01*___","d01*___","g01*___","d01*___"],
                          ["g01*___","g01*___","g01*___","g01*___","d01*___","d01*___","g01*___","g01*___"],
                          ["g01*___","g01*___","g01*___","g01*___","d01*___","d01*___","g01*E01","g01*___"],
                          ["g01*___","d01*___","g01*E01","g01*___","d01*___","d01*___","g01*___","g01*___"],
                          ["g01*___","g01*___","g01*___","g01*___","d01*___","d01*___","g01*___","g01*___"],
                          ["g01*E01","g01*___","g01*___","g01*___","d01*___","d01*___","g01*___","g01*___"]]
                          
        enemy_count = 0
        player_count = 0
        for tile in loaded_grid_tile_info:
            if tile[4] == "E":
                enemy_count += 1
            elif tile[4] == "P":
                player_count += 1

        player_characters = []
        enemy_characters = []

        for i in range(1,enemy_count):
            enemy_characters.append(map_Data.Character([], "Test Name", i, 1, 5, 5, 1, 0, 1, [], []))

        for i in range(1,player_count):
            player_characters.append(map_Data.Character([], "Test Name", i, 1, 5, 5, 1, 0, 1, [], []))

        self.battle_grid = map_Data.Battle_Grid(loaded_grid_tile_info, player_characters, enemy_characters)

        # Calculate the dynamic tile size
        # minimum of the height and breadth because the tiles will always be square and could thus not fit into the screen
        self.tile_size = min(self.window_width // self.board_dimensions[0], self.window_height // self.board_dimensions[1])

        self.tiles = map_Display.Tiles(self.surface, self.battle_grid.grid_tile_info, self.tile_size, self.window_width, self.window_height)
        self.characters = map_Display.Characters_Display(self.surface, self.battle_grid.grid_tile_info, self.tile_size, self.window_width, self.window_height)

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

    def update(self):
        """
        Update the game state. Currently does nothing, but can be extended.
        """
        self.tiles.load_data(self.battle_grid.grid_tile_info)
        self.characters.load_data(self.battle_grid.grid_tile_info)
        

    def get_map_data(self):
        
        


        pass

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