import pygame
import random
from components.Text import Text
from components.Game import Game
from components.Revolver import Revolver

# Initialize pygame
pygame.init()

# Setting up screen
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("HollowChamber")

FPS = 60
clock = pygame.time.Clock()

running = True
starting = True
playing = False
chosenOpp = None
mainGame = Game(display_surface)

# Playing Variables
isPlayerTurn = True
spunRevolver = False
canShoot = None
lostGame = False
wonGame = False
action_time = 0
wait_time = 1000  # 1 second wait time for actions
miss_display_time = 0
miss_display_duration = 1000  # 1 second

# Load button images
spin_button_img = pygame.image.load("assets/spin_button.png")
spin_button_img = pygame.transform.scale(spin_button_img, (150, 150))
shoot_yourself_button_img = pygame.image.load("assets/shoot_yourself_button.png")
shoot_yourself_button_img = pygame.transform.scale(shoot_yourself_button_img, (200, 200))
shoot_opponent_button_img = pygame.image.load("assets/shoot_opponent_button.png")
shoot_opponent_button_img = pygame.transform.scale(shoot_opponent_button_img, (200, 200))

# Create rects for buttons
spin_button_rect = spin_button_img.get_rect(topleft=(1080, 300))
shoot_yourself_button_rect = shoot_yourself_button_img.get_rect(topleft=(1080, 210))
shoot_opponent_button_rect = shoot_opponent_button_img.get_rect(topleft=(1080, 440))

# Load hit and miss signs
hit_sign_img = pygame.image.load("assets/miss_image.png")
hit_sign_img = pygame.transform.scale(hit_sign_img, (100, 100))
miss_sign_img = pygame.image.load("assets/miss_image.png")
miss_sign_img = pygame.transform.scale(miss_sign_img, (100, 100))

# Load sounds
click_sound = pygame.mixer.Sound("assets/clicksound.mp3")
shot_sound = pygame.mixer.Sound("assets/shotsound.mp3")
miss_sound = pygame.mixer.Sound("assets/misssound.mp3")
background_music = pygame.mixer.Sound("assets/bgmusic.mp3")
pygame.mixer.Sound.play(background_music, loops=-1)

winScreen = pygame.image.load("assets/WinScreen.png")
winScreen = pygame.transform.scale(winScreen, [1280, 800])
loseScreen = pygame.image.load("assets/LoseScreen.png")
loseScreen = pygame.transform.scale(loseScreen, [1280, 800])

def spinDice():
    return random.randint(1, 6)

def renderOpponentSelection():
    mainGame.drawStartScreen()
    if chosenOpp:
        # Highlight the chosen opponent
        pygame.draw.rect(display_surface, (0, 255, 0), chosenOpp.rect, 5)  # Green border
        message = Text(640, 700, f"You have chosen {chosenOpp.name}", (255, 255, 255), 36)
        message.show(display_surface)

while running:
    display_surface.fill((0, 0, 0))  # Clear screen

    current_time = pygame.time.get_ticks()

    if lostGame:
        display_surface.blit(loseScreen, [0, 0])
    elif wonGame:
        display_surface.blit(winScreen, [0, 0])
    else:
        if starting:
            renderOpponentSelection()
        elif playing:
            mainGame.drawPlayScreen(chosenOpp)

            if isPlayerTurn:
                if not spunRevolver:
                    display_surface.blit(spin_button_img, spin_button_rect.topleft)
                else:
                    display_surface.blit(shoot_yourself_button_img, shoot_yourself_button_rect.topleft)
                    display_surface.blit(shoot_opponent_button_img, shoot_opponent_button_rect.topleft)

            # Display the miss sign if it should be shown
            if current_time - miss_display_time <= miss_display_duration:
                display_surface.blit(miss_sign_img, (50, 375))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if starting and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for opp in mainGame.opponentsGroup:
                if opp.rect.collidepoint(pos):
                    pygame.mixer.Sound.play(click_sound)
                    chosenOpp = opp
                    starting = False
                    playing = True
                    mainGame.startTime = pygame.time.get_ticks()
        elif playing and current_time - action_time > wait_time and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if isPlayerTurn:
                if not spunRevolver:
                    if spin_button_rect.collidepoint(pos):
                        pygame.mixer.Sound.play(click_sound)
                        canShoot = mainGame.Revolver.canShoot(spinDice())
                        spunRevolver = True
                        action_time = current_time
                else:
                    if shoot_yourself_button_rect.collidepoint(pos):
                        pygame.mixer.Sound.play(click_sound)
                        if canShoot:
                            pygame.mixer.Sound.play(shot_sound)
                            lostGame = True
                        else:
                            pygame.mixer.Sound.play(miss_sound)
                            miss_display_time = current_time
                            spunRevolver = False
                        action_time = current_time
                    elif shoot_opponent_button_rect.collidepoint(pos):
                        pygame.mixer.Sound.play(click_sound)
                        if canShoot:
                            pygame.mixer.Sound.play(shot_sound)
                            wonGame = True
                        else:
                            pygame.mixer.Sound.play(miss_sound)
                            miss_display_time = current_time
                            isPlayerTurn = False
                            spunRevolver = False
                        action_time = current_time
            else:
                pygame.mixer.Sound.play(click_sound)
                canShoot = mainGame.Revolver.canShoot(spinDice())
                oppAnswer = chosenOpp.nextMove(mainGame.Revolver)
                if canShoot:
                    pygame.mixer.Sound.play(shot_sound)
                    if oppAnswer:
                        lostGame = True
                    else:
                        wonGame = True
                else:
                    pygame.mixer.Sound.play(miss_sound)
                    miss_display_time = current_time
                    isPlayerTurn = True
                action_time = current_time

    pygame.display.update()
    clock.tick(FPS)
