import pygame

class Bubble(pygame.sprite.Sprite):
    def __init__(self,centerx,centery,bubbleWidth):
        super().__init__()
        self.image = pygame.image.load("assets/SpeechBubble.png")
        self.image = pygame.transform.scale(self.image,[bubbleWidth,290])
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def show(self,screen):
        screen.blit(self.image,self.rect)