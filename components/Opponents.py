import pygame
from components.Text import Text
import random

class Opponents(pygame.sprite.Sprite):
    def __init__(self,name,display):
        super().__init__()
        self.display = display
        self.name = name
        self.image = pygame.image.load("assets/"+self.name+".png")
        self.image = pygame.transform.scale(self.image,[400,400])
        self.rect = self.image.get_rect()
       
    
    def renderStart(self,x,y):
        self.image = pygame.transform.scale(self.image,[250,250])
        self.rect.centerx = x
        self.rect.centery = y

        text = Text(self.rect.centerx-75,self.rect.centery+100,self.name,(255,255,255),34)
        
        self.display.blit(self.image, self.rect)
        text.show(self.display)

    def renderPlaying(self):
        self.image = pygame.transform.scale(self.image,[400,400])
        self.rect.centerx = 640
        self.rect.centery = 300

        text = Text(self.rect.centerx,self.rect.centery+self.textDiff,self.name,(255,255,255),34)
        text.show(self.display)
        self.display.blit(self.image, self.rect)



    def nextMove(revolver):
        pass

    def speak():
        pass
    

class RiskyRick(Opponents):
    def __init__(self,display):
        super().__init__("RiskyRick",display)
        self.startMessage = "Heh... what's the worst that could happen?"
        self.bubbleWidth = 600
        self.textDiff = 195


    def nextMove():
        chance = random.randint(1,10)
        if(chance <= 8 and chance >= 1):
            return True
        return False
        

class MathyMartha(Opponents):
    def __init__(self,display):
        super().__init__("MathyMartha",display)
        self.startMessage = "Erm... according to my calculations, you are dead."
        self.bubbleWidth = 700
        self.textDiff = 165

    def nextMove():
        
        pass
    
    
class AggressiveAlex(Opponents):
    def __init__(self,display):
        super().__init__("AggressiveAlex",display)
        self.startMessage = "HAHAHAHAHA YOU'RE FINISHED"
        self.bubbleWidth = 380
        self.textDiff = 230

    def nextMove():
        pass


class CautiousCarl(Opponents):
    def __init__(self,display):
        super().__init__("CautiousCarl",display)
        self.startMessage = "Uh.. uhm.. please have some mercy..."
        self.bubbleWidth = 500
        self.textDiff = 195

    def nextMove():
        pass

class BluffingBetty(Opponents):
    def __init__(self,display):
        super().__init__("BluffingBetty",display)
        self.startMessage = "Good luck kid, you're going to need it."
        self.bubbleWidth = 500
        self.textDiff = 185

    def nextMove():
        pass
   

    


    


    