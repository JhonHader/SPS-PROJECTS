import pygame
import time

class Board():

    BLOCK_SIZE = 10 # Las constantes se pueden crear por fuera del init

    WHITE = (0, 0, 0)
    YELLOW = (0, 0, 0)
    BLACK = (0, 0, 0)
    RED = (0, 0, 0)
    GREEN = (0, 0, 0)
    BLUE = (0, 0, 0)

    FONT_STYLE = 0
    __score_style = 0

    DISPLAY_WIDTH = 0
    DISPLAY_HEIGHT = 0

    DISPLAY = 0

    __clock = 0

    def __init__(self): # Muy biwn el init

        # Recomendacion: Para las constantes no poner __ y usarlas en mayusculas
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 102)
        self.BLACK = (0, 0, 0)
        self.RED = (213, 50, 80)
        self.GREEN = (0, 255, 0)
        self.BLUE = (50, 153, 213)

        self.FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
        self.SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

        self.DISPLAY_WIDTH = 600
        self.DISPLAY_HEIGHT = 400

        self.DISPLAY = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        pygame.display.set_caption('Snake by IEEE SPS')

        self.__clock = pygame.time.Clock()

    def updateBoard(self, snake, food) -> bool:
        """
        Return : True or false if the snake crashed
        """
        self.fill()
        self.show_food(food.getPositionX(), food.getPositionY())
        self.show_snake(snake.getBody())
        self.show_your_score(snake.getLength())
        self.refresh(snake.getSpeed())

        return self.checkSnakeCrashBoundaries(snake.getSnakeHeadPositionX(), snake.getSnakeHeadPositionY())

    def checkSnakeCrashBoundaries(self, snakeHeadPositionX, snakeHeadPositionY):
        if snakeHeadPositionX >= self.DISPLAY_WIDTH or snakeHeadPositionX < 0 or snakeHeadPositionY >= self.DISPLAY_HEIGHT or snakeHeadPositionY < 0:
            return True
        else:
            return False

    def message(self, msg): # Bien que toda la responsabilidad de pintar en la pantalla la tenga esta clase
        mesg = self.FONT_STYLE.render(msg, True, self.WHITE)
        self.DISPLAY.blit(mesg, [self.DISPLAY_WIDTH /3.8, self.DISPLAY_HEIGHT / 2])

    def show_your_score(self, snakeLength):
        value = self.SCORE_FONT.render(" " + str(snakeLength - 1), True, self.YELLOW)
        self.DISPLAY.blit(value, [0, 0])

    def show_snake(self, snakeBody):
        for block in snakeBody:
            pygame.draw.rect(self.DISPLAY, self.GREEN, [block[0], block[1], self.BLOCK_SIZE, self.BLOCK_SIZE])

    def show_food(self, foodPositionX, foodPositionY):
        pygame.draw.rect(self.DISPLAY, self.RED, [foodPositionX, foodPositionY, self.BLOCK_SIZE, self.BLOCK_SIZE])

    def refresh(self, snakeSpeed):
        self.__clock.tick(snakeSpeed)

    def fill(self):
        self.DISPLAY.fill(self.BLACK)