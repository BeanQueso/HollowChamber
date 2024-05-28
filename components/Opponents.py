import pygame
from components.Text import Text
from components.Bubble import Bubble
import random

class Opponents(pygame.sprite.Sprite):
    def __init__(self, name, display):
        super().__init__()
        self.display = display
        self.name = name
        self.image = pygame.image.load("assets/" + self.name + ".png")
        self.image = pygame.transform.scale(self.image, [400, 400])
        self.rect = self.image.get_rect()

    def renderStart(self, x, y):
        self.image = pygame.transform.scale(self.image, [250, 250])
        self.rect.centerx = x
        self.rect.centery = y

        text = Text(self.rect.centerx - 75, self.rect.centery + 100, self.name, (255, 255, 255), 34)

        self.display.blit(self.image, self.rect)
        text.show(self.display)

    def renderPlaying(self):
        self.image = pygame.transform.scale(self.image, [400, 400])
        self.rect.centerx = 640
        self.rect.centery = 300

        text = Text(self.rect.centerx, self.rect.centery + self.textDiff, self.name, (255, 255, 255), 34)
        text.show(self.display)
        self.display.blit(self.image, self.rect)

    def nextMove(self, revolver):
        pass

    def speak(self, message, display):
        startBubble = Bubble(self.rect.x + self.rect.width / 2, self.rect.y - 50, self.bubbleWidth)
        startMessage = Text(startBubble.rect.centerx, startBubble.rect.centery, message, (0, 0, 0), 28)

        startBubble.show(display)
        startMessage.show(display)
        # True -> shoot urself, False -> shoot other


class RiskyRick(Opponents):
    def __init__(self, display):
        super().__init__("RiskyRick", display)
        self.startMessage = "Heh... what's the worst that could happen?"
        self.bubbleWidth = 600
        self.textDiff = 195

    def nextMove(self, revolver):
        chance = random.random()
        return chance < 0.8  #80% chance to shoot himself


class MathyMartha(Opponents):
    def __init__(self, display):
        super().__init__("MathyMartha", display)
        self.startMessage = "Erm... according to my calculations, you are dead."
        self.bubbleWidth = 700
        self.textDiff = 165

    def nextMove(self, revolver):
        chance = revolver.getChances()
        weightedChance = chance + random.uniform(0, 0.5)  # a little randomness -> chance is 1/unfiredchambers
        return weightedChance < 1.3


class AggressiveAlex(Opponents):
    def __init__(self, display):
        super().__init__("AggressiveAlex", display)
        self.startMessage = "HAHAHAHAHA YOU'RE FINISHED"
        self.bubbleWidth = 380
        self.textDiff = 230

    def nextMove(self, revolver):
        chance = random.random()
        return chance > 0.1  #90% chance, very aggressive


class CautiousCarl(Opponents):
    def __init__(self, display):
        super().__init__("CautiousCarl", display)
        self.startMessage = "Uh.. uhm.. please have some mercy..."
        self.bubbleWidth = 500
        self.textDiff = 195

    def nextMove(self, revolver):
        chance = random.random()
        return chance < 0.1  #10%chance, scared


class BluffingBetty(Opponents):
    def __init__(self, display):
        super().__init__("BluffingBetty", display)
        self.startMessage = "Good luck kid, you're going to need it."
        self.bubbleWidth = 500
        self.textDiff = 185

    def nextMove(self, revolver):
        chance = random.random()
        return chance < 0.5  #50% chance,unpredictable
