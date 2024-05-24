import random

class Revolver():
    
    def __init__(self,maxCapacity):
        self.previousIndices = [False] * maxCapacity
        self.revolverIndex = random.randint(1,maxCapacity) - 1;
        self.myIndex = random.randint(1,maxCapacity) - 1;
        self.maxCapacity = maxCapacity
    
    def spinRevolver(self,spins):
        for i in range(spins):
            self.myIndex = random.randint(1,self.maxCapacity) - 1;

    def canShoot(self,spins):
        self.spinRevolver(spins)
        if(self.myIndex == self.revolverIndex):
            return True
        return False

    def getChances(self):
        for i in self.previousIndices:
            if(i):


    



    



        

            
                
            
            
