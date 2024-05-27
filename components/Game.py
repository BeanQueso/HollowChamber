import random
import pygame

from components.Text import Text
from components.Revolver import Revolver
from components.Player import Player
from components.Bubble import Bubble
from components.Opponents import MathyMartha
from components.Opponents import RiskyRick
from components.Opponents import AggressiveAlex
from components.Opponents import CautiousCarl
from components.Opponents import BluffingBetty


class Game():
    def __init__(self, display):
        self.display = display
        self.Revolver = Revolver(6)
        self.isPlayerTurn = True
        self.isShootingSelf = None
        self.answer = None
        self.madeChoice = False
        self.hasSpinned = False

        marthaCharacter = MathyMartha(self.display)
        rickCharacter = RiskyRick(self.display)
        alexCharacter = AggressiveAlex(self.display)
        carlCharacter = CautiousCarl(self.display)
        bettyCharacter = BluffingBetty(self.display)

        self.opponentsGroup = pygame.sprite.Group()

        self.opponentsGroup.add(marthaCharacter)
        self.opponentsGroup.add(rickCharacter)
        self.opponentsGroup.add(alexCharacter)
        self.opponentsGroup.add(carlCharacter)
        self.opponentsGroup.add(bettyCharacter)

        self.player = Player(640, 600)
        self.playerGroup = pygame.sprite.Group()

        self.playerGroup.add(self.player)

    def drawStartScreen(self):
        self.display.fill((50, 0, 20))

        welcomeText = Text(640, 100, "Hollow Chamber", (255, 0, 0), 130)
        welcomeText.show(self.display)

        optionText = Text(640, 180, "Choose your operator",
                          (255, 255, 255), 34)
        optionText.show(self.display)

        x = 230

        for i in self.opponentsGroup:
            i.renderStart(x, 600)
            x += 240

    def drawPlayScreen(self, opponent):
        self.display.fill((50, 0, 20))
        opponent.renderPlaying()

        startBubble = Bubble(opponent.rect.x+opponent.rect.width/2,
                             opponent.rect.y-50, opponent.bubbleWidth)
        startMessage = Text(startBubble.rect.centerx,
                            startBubble.rect.centery, opponent.startMessage, (0, 0, 0), 28)

        startBubble.show(self.display)
        startMessage.show(self.display)

        self.playerGroup.draw(self.display)

        playerResponse = Text(self.player.rect.centerx+200,
                              self.player.rect.centery, "Nuh uh.", (0, 0, 0), 28)
        playerBubble = Bubble(playerResponse.text_rect.centerx,
                              playerResponse.text_rect.centery, 100)

        playerBubble.show(self.display)
        playerResponse.show(self.display)

        self.doGameLoop(opponent)

    def rollDice(self):
        return random.randint(1, 6)

    def doGameLoop(self, opp):
        if self.isPlayerTurn:
            self.player.speak("Hmm...", self.display)
            opp.speak("Your Turn", self.display)

            if not self.madeChoice:
                if not self.hasSpinned:
                    opp.speak("Spin the Revolver Little Boy...", self.display)
                    t0 = Text(200, 400, "Spin Revovler", (255, 255, 255), 50)
                    t0.show(self.display)
                else:
                    t1 = Text(200, 400, "Shoot Yourself", (255, 255, 255), 50)
                    t1.show(self.display)
                    t2 = Text(1080, 400, "Shoot Opponent", (255, 255, 255), 50)
                    t2.show(self.display)
                for event in pygame.event.get():

                    pos = pygame.mouse.get_pos()

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if not self.hasSpinned:
                            if t0.text_rect.collidepoint(pos):
                                spins = self.rollDice()
                                self.answer = self.Revolver.canShoot(spins)
                                print("Spinned")
                                self.hasSpinned = True
                        else:
                            if t1.text_rect.collidepoint(pos):
                                self.isShootingSelf = True
                                self.madeChoice = True
                                print("Shot MYself")
                            elif t2.text_rect.collidepoint(pos):
                                self.isShootingSelf = False
                                self.madeChoice = True
                                print("Shot the other persn")

            if self.madeChoice:
                print(self.answer)
                if self.answer and self.isShootingSelf:
                    # Go To Death Screen
                    self.display.fill((0, 0, 0))
                    print("YOu DieD HAHAHAHAHA")

                    return False
                elif self.answer and not self.isShootingSelf:
                    # Go to Win Screen
                    print("YOu WON HAHAHAHAHA")
                    self.display.fill((255, 255, 255))
                    return True
                elif not self.answer and not self.isShootingSelf:
                    # Changes the turn to the opp
                    print("Changed Turn")
                    self.isPlayerTurn = False
                    self.madeChoice = False
                    opp.speak(
                        "My Turn...", self.display)
                    self.hasSpinned = False

                else:
                    self.madeChoice = False
                    self.hasSpinned = False

        elif not self.isPlayerTurn:
            print("IS it my turn?")
            opp.speak("My TURN HAHAHAHHA", self.display)
            spins = self.rollDice()
            self.answer = self.Revolver.canShoot(spins)
            self.isShootingSelf = opp.nextMove(self.Revolver)

            if self.answer and self.isShootingSelf:
                # Go To Win Screen
                opp.speak("OHHH.... You Have defeated me", self.display)

                print("YOu WON AHHHHHHHH")
                return
            elif self.answer and not self.isShootingSelf:
                # Go to LOse Screen
                opp.speak("HAHAHHAHAHA DIEEEE HAHAHAHAHAHAHA", self.display)

                print("YOu LOST AAHHHHHHHAHAHAHAHA")
                return
            elif not self.answer and not self.isShootingSelf:
                # Changes the turn to the opp

                print("Changed Turn")
                self.isPlayerTurn = True
                opp.speak("Your Turn", self.display)
