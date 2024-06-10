import pygame
import frontend
import backend
import os
import Map_Display




# Example file showing a basic pygame "game loop"
# pygame setup
pygame.init()

# Retrieves the python file directory 
script_dir = os.path.dirname(__file__)

# Get the screen resolution
screen_info = pygame.display.Info()
screen_width = int(screen_info.current_w*0.8)
screen_height = int(screen_info.current_h*0.8)

Map_Display.window_height= screen_height
Map_Display.window_width= screen_width


# Set the display mode to the 80% of the screen resolution
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle Sim")


clock = pygame.time.Clock()
running = True
dt = 0

# Variable to keep track of mouse click locations
mouse_x, mouse_y = -1,-1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

    # fill the screen with an image
    room_1_image_path = os.path.join(script_dir, 'Media', 'Image', 'Room1.png')
    background_image = pygame.image.load(room_1_image_path)
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    screen.blit(background_image, (0, 0))
    

    # RENDER YOUR GAME HERE

#------------------------------------------------------------------------------------------------------------
    

   

    # Dynamically adjusts button height and width based on screen size ie. always a third of the screen size
    button_width = screen_width//3
    button_height = screen_height//3

# Excelsior, lets try once more with feeling
    #image pathway load in
    image_path = "Media/Image/Neutral.jpg"
    image = pygame.image.load(image_path)
   #height and width
    new_width=200
    new_height=150
    #creating the centered rectangle for the loaded image
    image_rect= image.get_rect()
    imagex = (screen_width - new_width)/2
    imagey = (screen_height - new_height)/2
    image_rect.center = (imagex, imagey)
    #resize the image
    resized_image = pygame.transform.scale(image, (new_width, new_height))
    #update screen position with the resized image and centered position
    screen.blit (resized_image, image_rect.center)




    # Construct relative paths to your image files
    rock_image_path = os.path.join(script_dir, 'Media', 'Image', 'Rock_button.png')
    paper_image_path = os.path.join(script_dir, 'Media', 'Image', 'Paper_button.png')
    scissors_image_path = os.path.join(script_dir, 'Media', 'Image', 'Scissors_button.png')
    

    # Creating button instances and drawing them on the screen
    button_Rock = frontend.button(screen,"blue", 0, screen_height-button_height, button_width, button_height,10000,rock_image_path)
    button_Rock.draw_button()

    button_Paper = frontend.button(screen,"Red", button_width, screen_height-button_height, button_width, button_height,10000,paper_image_path)
    button_Paper.draw_button()

    button_Scissors = frontend.button(screen,"Green", button_width*2, screen_height-button_height, button_width, button_height,10000,scissors_image_path)
    button_Scissors.draw_button()

    if button_Rock.coordinates[0] <= mouse_x <= button_Rock.coordinates[0] + button_Rock.width and button_Rock.coordinates[1] <= mouse_y <= button_Rock.coordinates[1] + button_Rock.height:
                print("Rock Button clicked!")

    if button_Paper.coordinates[0] <= mouse_x <= button_Paper.coordinates[0] + button_Paper.width and button_Paper.coordinates[1] <= mouse_y <= button_Paper.coordinates[1] + button_Paper.height:
                print("Paper Button clicked!")

    if button_Scissors.coordinates[0] <= mouse_x <= button_Scissors.coordinates[0] + button_Scissors.width and button_Scissors.coordinates[1] <= mouse_y <= button_Scissors.coordinates[1] + button_Scissors.height:
                print("Scissors Button clicked!")
                #Test example of menu button being clicked and opening up the game
                mygame = Map_Display.Game()
                mygame.main()
                running=False

#-----------------------------------------------------------------------------------------------------
    # Resets mouse click locations after each loop
    mouse_x, mouse_y = -1,-1


#-------------------------------------------------------------------------------------------------------------    

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt=clock.tick(60)/1000 # limits FPS to 60

pygame.quit()


