import pygame
import backend

# Example file showing a basic pygame "game loop"
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt=0

# Initialized Rock, Paper, Scissors bot object
RPS_bot = backend.RPS_bot()

#Here it seems to put the position of the player in the centre of the screen
player_pos= pygame.Vector2 (screen.get_width()/2,screen.get_height()/2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    #DRAWING THE PLAYER POSITION: Over here we can put the player position
    #Currently testing out: Adjusting the last number "40" increases the radius/Size of the circle
    #Can switch out the player_pos for a coordinate on the screen or create it relative to player with something like (player_pos)+(00,-100)
    pygame.draw.circle(screen,"red",player_pos,40)
   
    #Next up Im checking and testing through the inputs, this allows the circle to move, adjusting numbers allows it to move faster
    keys= pygame.key.get_pressed()
    if keys [pygame.K_w]: player_pos.y -=600*dt
    if keys [pygame.K_s]: player_pos.y +=600*dt
    if keys [pygame.K_a]: player_pos.x -=600*dt
    if keys [pygame.K_d]: player_pos.x +=600*dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    dt=clock.tick(60)/1000 # limits FPS to 60, and the speed by which the circle can move within a given frame

pygame.quit()