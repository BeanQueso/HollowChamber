import pygame
import random
import math
import components.Game as Game


#initialise python
pygame.init()

#setting up screen
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("HollowChamber")

FPS = 60
clock = pygame.time.Clock()

def update(self,surface):
    pygame.draw.rect(surface, (255,255,255),pygame.Rect(self.centerx,self.centery,self.width,self.height))

running = True

starting = True

mainGame = Game.Game(display_surface)


while running:
    
    #Draw the orignal backgorund
    #Draw the opponent
    #Draw the player
    #If player turn: Spin reveovler and let player choose
    # If Opponent turn: Spin revovler and let Ai choose    


    display_surface.fill((100,100,100))
    #wallGroup.update(display_surface)

    if starting:
        mainGame.drawStartScreen()

    pygame.display.update()
    clock.tick(FPS)
