import random

# Bot that plays rock, paper or scissors
class RPS_bot:

    def __init__(self):

        self.wins = 10
        

        return
    
    # Makes a move randomly
    def make_random_move(self):
        wins = 5
        print(self.wins)
        print(wins)
        return random.choice(['R', 'P', 'S'])

