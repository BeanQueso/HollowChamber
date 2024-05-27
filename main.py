import pygame
import random
import math
import components.Game as Game


# initialise python
pygame.init()

# setting up screen
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("HollowChamber")

FPS = 60
clock = pygame.time.Clock()


def update(self, surface):
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
        self.centerx, self.centery, self.width, self.height))


running = True

starting = True
playing = False

chosen = None

mainGame = Game.Game(display_surface)

while running:

    # Draw the orignal backgorund
    # Draw the opponent
    # Draw the player
    # If player turn: Spin reveovler and let player choose
    # If Opponent turn: Spin revovler and let Ai choose

    for event in pygame.event.get():  # over here im just checking if the
        if event.type == pygame.QUIT:
            running = False
        if starting:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and starting == True:
                pos = pygame.mouse.get_pos()
                for opp in mainGame.opponentsGroup:
                    if opp.rect.collidepoint(pos):
                        mainGame.startTime = pygame.time.get_ticks()
                        starting = False
                        playing = True
                        chosen = opp

    display_surface.fill((100, 100, 100))
    # wallGroup.update(display_surface)

    if starting:
        mainGame.drawStartScreen()

    if playing:
        mainGame.drawPlayScreen(chosen)

    pygame.display.update()
    clock.tick(FPS)
