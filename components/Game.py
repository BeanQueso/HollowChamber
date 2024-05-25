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
from components.Opponents import BluffingBetty



class Game():
    def __init__(self, display):
        self.display = display
        self.Revolver = Revolver.Revolver(6)

        self.marthaCharacter = MathyMartha(self.display)
        self.rickCharacter = RiskyRick(self.display)
        self.alexCharacter = AggressiveAlex(self.display)
        self.carlCharacter = CautiousCarl(self.display)
        self.bettyCharacter = BluffingBetty(self.display)

        self.opponentsGroup = pygame.sprite.Group()

        self.opponentsGroup.add(self.marthaCharacter)
        self.opponentsGroup.add(self.rickCharacter)
        self.opponentsGroup.add(self.alexCharacter)
        self.opponentsGroup.add(self.carlCharacter)
        self.opponentsGroup.add(self.bettyCharacter)

        

    def drawStartScreen(self):
        self.display.fill((50,0,20))

        welcomeText = Text.Text(640,100,"Hollow Chamber",(255,0,0),130)
        welcomeText.show(self.display)

        optionText = Text.Text(640,180,"Choose your operator",(255,255,255),34)
        optionText.show(self.display)

        x = 230

        for i in self.opponentsGroup:
            i.renderStart(x,600)
            x+=240


    def drawPlayScreen(self,opponent):
        
        pass

        
        
    def rollDice(self):
        return random.randint(1,6)
   
    
