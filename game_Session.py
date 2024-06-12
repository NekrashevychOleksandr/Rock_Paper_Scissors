import pygame
import map_Display


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
        self.BG_COLOR = ("green")
        self.running = True

        # Default board dimensions will be pulled from a file later
        self.board_dimensions = [8,8]

        # Calculate the dynamic tile size
        # minimum of the height and breadth because the tiles will always be square and could thus not fit into the screen
        self.tile_size = min(self.window_width // self.board_dimensions[0], self.window_height // self.board_dimensions[1])

        self.tiles = map_Display.Tiles(self.surface, self.board_dimensions, self.tile_size, self.window_width, self.window_height)
        self.characters = map_Display.Characters_Display(self.surface, self.board_dimensions, self.tile_size, self.window_width, self.window_height)

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