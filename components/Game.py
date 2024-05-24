import random
import components.Text as Text
import components.Revolver as Revolver
import pygame
from components import Player
from components import Walls
from components.Opponents import MathyMartha
from components.Opponents import RiskyRick
from components.Opponents import AggressiveAlex
from components.Opponents import CautiousCarl



class Game():
    def __init__(self, display):
        self.display = display
        self.Revolver = Revolver.Revolver(6)

        self.marthaCharacter = MathyMartha(self.display)
        self.rickCharacter = RiskyRick(self.display)
        self.alexCharacter = AggressiveAlex(self.display)
        self.carlCharacter = CautiousCarl(self.display)
        

    def drawStartScreen(self):
        self.display.fill((50,0,20))

        welcomeText = Text.Text(640,100,"Hollow Chamber",(255,0,0),130)
        welcomeText.show(self.display)

        optionText = Text.Text(640,180,"Choose your operator",(255,255,255),34)
        optionText.show(self.display)

        self.marthaCharacter.renderStart(230,600)
        self.rickCharacter.renderStart(470,600)
        self.alexCharacter.renderStart(710,600)
        self.carlCharacter.renderStart(950,600)


    def drawPlayScreen(self,opponent):
        
        pass

        
        
    def rollDice(self):
        return random.randint(1,6)
   
    
