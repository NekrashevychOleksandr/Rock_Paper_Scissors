import pygame

class button:

    def __init__(self, screen, colour, x,y, width, height, thickness, image_path = None):
        self.screen = screen
        self.coordinates = [x,y]
        self.colour = colour
        self.width = width
        self.height = height
        self.thickness = thickness
        self.image_path = image_path
        

        if image_path:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            self.image = None

    def draw_button(self):
        # Draw the button border
        pygame.draw.rect(self.screen, self.colour, (self.coordinates[0], self.coordinates[1], self.width, self.height), self.thickness)
        
        # Blit the image if available
        if self.image:
            self.screen.blit(self.image, (self.coordinates[0], self.coordinates[1]))


class player_sprite(pygame.sprite.Sprite):
    def __init__(self, x,y, image_path):
        self.position = (x, y)
        self.image = pygame.image.load(image_path)

 
    def draw (self, surface):
        surface.blit(self.image, self.position)