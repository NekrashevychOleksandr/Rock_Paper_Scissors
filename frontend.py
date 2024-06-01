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

    
