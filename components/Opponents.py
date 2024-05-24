import pygame
import components.Text as Text
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

        self.text = Text.Text(self.rect.centerx-75,self.rect.centery+100,self.name,(255,255,255),34)
        
        self.display.blit(self.image, self.rect)
        self.text.show(self.display)



    def nextMove(revolver):
        pass

    def speak():
        pass
    

class RiskyRick(Opponents):
    def __init__(self,display):
        super().__init__("RiskyRick",display)

    def nextMove():
        chance = random.randint(1,10)
        if(chance <= 8 and chance >= 1):
            return True
        return False
        

class MathyMartha(Opponents):
    def __init__(self,display):
        super().__init__("MathyMartha",display)
    
    def nextMove():
        
        pass
    
    
class AggressiveAlex(Opponents):
    def __init__(self,display):
        super().__init__("AggressiveAlex",display)

    def nextMove():
        pass
   

    


    


    