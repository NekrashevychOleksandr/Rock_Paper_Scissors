import pygame

class button:

    def __init__(self, screen, colour, x,y, width, height, thickness):
        self.screen = screen
        self.coordinates = [x,y]
        self.colour = colour
        self.width = width
        self.height = height
        self.thickness = thickness
        

    def draw_button_border_rect(self):
        pygame.draw.rect(self.screen, self.colour, (self.coordinates[0], self.coordinates[1], self.width, self.height), self.thickness)
        return


class player_sprite(pygame.sprite.Sprite):
    def __init__(self, x,y, image_path):
        self.position = (x, y)
        self.image = pygame.image.load(image_path)

 
    def draw (self, surface):
        surface.blit(self.image, self.position)