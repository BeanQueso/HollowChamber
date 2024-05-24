import pygame

class Walls(pygame.sprite.Sprite):
    def __init__(self,centerx,centery,width,height):
        super().__init__()
        self.centerx = centerx
        self.centery = centery
        self.width = width
        self.height = height