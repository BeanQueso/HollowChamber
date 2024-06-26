import random

class Revolver:
    def __init__(self, maxCapacity):
        self.previousShots = [False] * maxCapacity
        self.revolverIndex = random.randint(0, maxCapacity - 1)
        self.myIndex = random.randint(0, maxCapacity - 1)
        self.maxCapacity = maxCapacity

    def spinRevolver(self, spins): # spins decided by the dice rolled
        for _ in range(spins):
            if self.myIndex == self.maxCapacity - 1:
                self.myIndex = 0
            else:
                self.myIndex += 1

    def canShoot(self, spins): # will return whether or not the gun will shoot a bullet
        self.spinRevolver(spins)
        if self.myIndex == self.revolverIndex and not self.previousShots[self.myIndex]:
            return True
        self.previousShots[self.myIndex] = True
        return False

    def getChances(self):
        unfired_chambers = self.previousShots.count(False)
        if unfired_chambers > 0:
            return 1 / unfired_chambers
        else:
            return 0


