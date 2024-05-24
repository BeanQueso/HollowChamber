import random

class Dice():
    def __init__(self):
        self.sides = 6
    
    def rollDice(self):
        return random.randint(1,6)

    