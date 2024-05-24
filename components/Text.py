import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self,centerx,centery,text,textcolor,fontsize):
        super().__init__()
        self.font = pygame.font.Font("Abrushow.otf",fontsize)

        self.text = self.font.render(text,True,textcolor)
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = centerx
        self.text_rect.centery = centery

    def show(self,screen):
        screen.blit(self.text,self.text_rect)