import pygame
import frontend
import backend

# Example file showing a basic pygame "game loop"
# pygame setup
pygame.init()




# Get the screen resolution
screen_info = pygame.display.Info()
screen_width = int(screen_info.current_w*0.8)
screen_height = int(screen_info.current_h*0.8)




# Set the display mode to the 80% of the screen resolution
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")


clock = pygame.time.Clock()
running = True
dt=0

# Initialized Rock, Paper, Scissors bot object
RPS_bot = backend.RPS_bot()



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

#------------------------------------------------------------------------------------------------------------
    








#-------------------------------------------------------------------------------------------------------------    

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt=clock.tick(60)/1000 # limits FPS to 60, and the speed by which the circle can move within a given frame

pygame.quit()


