import random

class Food():

    __positionX = 0
    __positionY = 0

    def __init__(self, boardWidth, boardHeight, blockSize):
        self.restart(boardWidth, boardHeight, blockSize)

    def getPositionX(self):
        return self.__positionX
    
    def getPositionY(self):
        return self.__positionY
        
    def restart(self, boardWidth, boardHeight, blockSize):
        self.__positionX = round(random.randrange(0, boardWidth - blockSize) / 10.0) * 10.0
        self.__positionY = round(random.randrange(0, boardHeight - blockSize) / 10.0) * 10.0