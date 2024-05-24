import pygame

class Player(pygame.sprite.Sprite):
    #init function
    def __init__(self,centerx,centery):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image,[400,400])
        self.rect = self.image.get_rect()
        self.rect.x = centerx
        self.rect.y = centery