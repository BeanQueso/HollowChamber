import pygame
import random
from components.Text import Text
from components.Game import Game
from components.Bubble import Bubble

pygame.init()

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

isPlayerTurn = True
spunRevolver = False
canShoot = None
lostGame = False
wonGame = False
action_time = 0
wait_time = 1000 
miss_display_time = 0
miss_display_duration = 1000 

current_message = ""

spin_button_img = pygame.image.load("assets/spin_button.png")
spin_button_img = pygame.transform.scale(spin_button_img, (150, 150))
shoot_yourself_button_img = pygame.image.load("assets/shoot_yourself_button.png")
shoot_yourself_button_img = pygame.transform.scale(shoot_yourself_button_img, (200, 200))
shoot_opponent_button_img = pygame.image.load("assets/shoot_opponent_button.png")
shoot_opponent_button_img = pygame.transform.scale(shoot_opponent_button_img, (200, 200))
opponent_action_button_img = pygame.image.load("assets/opponent_action_button.png")
opponent_action_button_img = pygame.transform.scale(opponent_action_button_img, (200, 200))

spin_button_rect = spin_button_img.get_rect(topleft=(1080, 300))
shoot_yourself_button_rect = shoot_yourself_button_img.get_rect(topleft=(1080, 210))
shoot_opponent_button_rect = shoot_opponent_button_img.get_rect(topleft=(1080, 440))
opponent_action_button_rect = opponent_action_button_img.get_rect(topleft=(50, 190))

hit_sign_img = pygame.image.load("assets/miss_image.png")
hit_sign_img = pygame.transform.scale(hit_sign_img, (100, 100))
miss_sign_img = pygame.image.load("assets/miss_image.png")
miss_sign_img = pygame.transform.scale(miss_sign_img, (100, 100))

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
        intro_bubble = Bubble(chosenOpp.rect.centerx, 50, chosenOpp.bubbleWidth)
        intro_message = Text(intro_bubble.rect.centerx, intro_bubble.rect.centery, chosenOpp.startMessage, (0, 0, 0), 28)
        intro_bubble.show(display_surface)
        intro_message.show(display_surface)

def renderMessage():
    if chosenOpp and current_message:
        message_bubble = Bubble(chosenOpp.rect.centerx, 50, chosenOpp.bubbleWidth)
        message_text = Text(message_bubble.rect.centerx, message_bubble.rect.centery, current_message, (0, 0, 0), 28)
        message_bubble.show(display_surface)
        message_text.show(display_surface)

while running:
    display_surface.fill((0, 0, 0)) 

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
            else:
                display_surface.blit(opponent_action_button_img, opponent_action_button_rect.topleft)

            if current_time - miss_display_time <= miss_display_duration:
                display_surface.blit(miss_sign_img, (60, 540))
            renderMessage()

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
                    current_message = chosenOpp.startMessage
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
                            current_message = "Lucky... that was close"
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
                            # Change the message for the next action
                            current_message = "HA! YOU MISSED! MY TURN!"
                        action_time = current_time
            else:
                if opponent_action_button_rect.collidepoint(pos):
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
                        current_message = "Go ahead, your turn"
                    action_time = current_time

    pygame.display.update()
    clock.tick(FPS)
