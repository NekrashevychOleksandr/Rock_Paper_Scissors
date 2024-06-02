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
    
