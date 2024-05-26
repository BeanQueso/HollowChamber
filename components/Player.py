import pygame
from components.Text import Text
from components.Bubble import Bubble


class Player(pygame.sprite.Sprite):
    # init function
    def __init__(self, centerx, centery):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, [400, 400])
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def speak(self, message, display):
        playerResponse = Text(self.rect.centerx+200,
                              self.rect.centery, message, (0, 0, 0), 28)
        playerBubble = Bubble(playerResponse.text_rect.centerx,
                              playerResponse.text_rect.centery, 100)

        playerBubble.show(display)
        playerResponse.show(display)
