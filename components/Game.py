import random
import pygame

from components.Text import Text
from components.Revolver import Revolver
from components.Player import Player
from components.Bubble import Bubble
from components.Opponents import MathyMartha
from components.Opponents import RiskyRick
from components.Opponents import AggressiveAlex
from components.Opponents import CautiousCarl
from components.Opponents import BluffingBetty



class Game():
    def __init__(self, display):
        self.display = display
        self.Revolver = Revolver(6)

        marthaCharacter = MathyMartha(self.display)
        rickCharacter = RiskyRick(self.display)
        alexCharacter = AggressiveAlex(self.display)
        carlCharacter = CautiousCarl(self.display)
        bettyCharacter = BluffingBetty(self.display)

        self.opponentsGroup = pygame.sprite.Group()

        self.opponentsGroup.add(marthaCharacter)
        self.opponentsGroup.add(rickCharacter)
        self.opponentsGroup.add(alexCharacter)
        self.opponentsGroup.add(carlCharacter)
        self.opponentsGroup.add(bettyCharacter)

        self.player = Player(640,600)
        self.playerGroup = pygame.sprite.Group()

        self.playerGroup.add(self.player)

        

    def drawStartScreen(self):
        self.display.fill((50,0,20))

        welcomeText = Text(640,100,"Hollow Chamber",(255,0,0),130)
        welcomeText.show(self.display)

        optionText = Text(640,180,"Choose your operator",(255,255,255),34)
        optionText.show(self.display)

        x = 230

        for i in self.opponentsGroup:
            i.renderStart(x,600)
            x+=240


    def drawPlayScreen(self,opponent):
        self.display.fill((50,0,20))
        opponent.renderPlaying()

        startBubble = Bubble(opponent.rect.x+opponent.rect.width/2,opponent.rect.y-50,opponent.bubbleWidth)
        startMessage = Text(startBubble.rect.centerx,startBubble.rect.centery,opponent.startMessage, (0,0,0), 28) 

        startBubble.show(self.display)
        startMessage.show(self.display)

        self.playerGroup.draw(self.display)

        playerResponse = Text(self.player.rect.centerx+200,self.player.rect.centery, "Nuh uh.", (0,0,0),28)
        playerBubble = Bubble(playerResponse.text_rect.centerx,playerResponse.text_rect.centery, 100)

        playerBubble.show(self.display)
        playerResponse.show(self.display)


        
        
    def rollDice(self):
        return random.randint(1,6)
   
    
