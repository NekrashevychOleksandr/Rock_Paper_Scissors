import random
from PIL import Image
import matplotlib.pyplot as plt

# Bot that plays rock, paper or scissors
class RPS_bot:

    def __init__(self):
        self.wins = 10
    
    # Makes a move randomly
    def make_random_move(self):
        return random.choice(['R', 'P', 'S'])
    



#Below is display for a player hand, that throws rock, paper, scissors
    class move_display_player_1:
        def __init__(self, image_path):
            self.image_path= image_path
            self.image= None

        def load_image(self):
            if self.image:
                plt.imshow(self.image)
                plt.axis ('off')
                plt.show()
                pass