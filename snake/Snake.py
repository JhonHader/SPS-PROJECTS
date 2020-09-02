import random 

class Snake():

    __block_size = 0
    __snake_speed = 0
    __snake_body = []
    __snake_length = 0
    __snakeHeadPositionX = 0
    __snakeHeadPositionY = 0
    __origin = []
    __snakeHeadPositionX_change = 0
    __snakeHeadPositionY_change = 0

    def __init__(self, boardWidth, boardHeight, blockSize):
        self.__block_size = blockSize
        self.__snake_speed = 15 # Bien speed y length son nombres bastante claros y se puede deducir su funcionalidad
        self.__snake_length = 1
        self.__snakeHeadPositionX = boardWidth / 2
        self.__snakeHeadPositionY = boardHeight / 2
        self.__origin = [self.__snakeHeadPositionY, self.__snakeHeadPositionY]
        self.__snakeHeadPositionX_change = 0
        self.__snakeHeadPositionY_change = 0
        self.__snake_body = []

    def getSnakeHeadPositionX(self):
        return self.__snakeHeadPositionX

    def getSnakeHeadPositionY(self):
        return self.__snakeHeadPositionY

    def getBody(self):
        return self.__snake_body

    def getLength(self):
        return self.__snake_length
    
    def getSpeed(self):
        return self.__snake_speed

    def restart(self):
        self.__snake_length = 1
        self.__snakeHeadPositionX = self.__origin[0]
        self.__snakeHeadPositionY = self.__origin[1]
        self.__snakeHeadPositionX_change = 0
        self.__snakeHeadPositionY_change = 0
        self.__snake_body = []

    def change_direction(self, direction):

        # 0 - up, 1 - right, 2 - down, 3 - left

        if direction == 0:
            self.__snakeHeadPositionX_change = 0
            self.__snakeHeadPositionY_change = -self.__block_size
        elif direction == 1:
            self.__snakeHeadPositionX_change = self.__block_size
            self.__snakeHeadPositionY_change = 0
        elif direction == 2:
            self.__snakeHeadPositionX_change = 0
            self.__snakeHeadPositionY_change = self.__block_size
        elif direction == 3:
            self.__snakeHeadPositionX_change = -self.__block_size
            self.__snakeHeadPositionY_change = 0
        else:
            self.__snakeHeadPositionX_change = 0
            self.__snakeHeadPositionY_change = 0

    def crashed_boundaries(self, brd):
        if self.__snakeHeadPositionX >= brd._board__dis_width or self.__snakeHeadPositionX < 0 or self.__snakeHeadPositionY >= brd._board__dis_height or self.__snakeHeadPositionY < 0:
            return True
        else:
            return False

    def move(self):
        self.__snakeHeadPositionX += self.__snakeHeadPositionX_change
        self.__snakeHeadPositionY += self.__snakeHeadPositionY_change

    def crashed_itself(self):
        snake_Head = []
        snake_Head.append(self.__snakeHeadPositionX)
        snake_Head.append(self.__snakeHeadPositionY)
        self.__snake_body.append(snake_Head)
        if len(self.__snake_body) > self.__snake_length:
            del self.__snake_body[0]

        for x in self.__snake_body[:-1]:
            if x == snake_Head:
                return True

    def increaseLength(self):
        self.__snake_length += 1