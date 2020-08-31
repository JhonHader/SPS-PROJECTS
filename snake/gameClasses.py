import pygame
import time
import random

class board():

    __white = (0, 0, 0)
    __yellow = (0, 0, 0)
    __black = (0, 0, 0)
    __red = (0, 0, 0)
    __green = (0, 0, 0)
    __blue = (0, 0, 0)

    __font_style = 0
    __score_style = 0

    __dis_width = 0
    __dis_height = 0

    __dis = 0

    __clock = 0

    def __init__(self):
        self.__white = (255, 255, 255)
        self.__yellow = (255, 255, 102)
        self.__black = (0, 0, 0)
        self.__red = (213, 50, 80)
        self.__green = (0, 255, 0)
        self.__blue = (50, 153, 213)

        self.__font_style = pygame.font.SysFont("bahnschrift", 25)
        self.__score_font = pygame.font.SysFont("comicsansms", 35)

        self.__dis_width = 600
        self.__dis_height = 400

        self.__dis = pygame.display.set_mode((self.__dis_width, self.__dis_height))
        pygame.display.set_caption('Snake by IEEE SPS')

        self.__clock = pygame.time.Clock()

    def message(self, msg):
        mesg = self.__font_style.render(msg, True, self.__white)
        self.__dis.blit(mesg, [self.__dis_width /3.8, self.__dis_height / 2])

    def Your_score(self, snake):
        value = self.__score_font.render(" " + str(snake._snake__snake_length - 1), True, self.__yellow)
        self.__dis.blit(value, [0, 0])

    def show_snake(self, snk):
        for x in snk._snake__snake_list:
            pygame.draw.rect(self.__dis, self.__green, [x[0], x[1], snk._snake__snake_block, snk._snake__snake_block])

    def show_food(self, snk, fd):
        pygame.draw.rect(self.__dis, self.__red, [fd._food__foodx, fd._food__foody, snk._snake__snake_block, snk._snake__snake_block])

    def refresh(self, snk):
        self.__clock.tick(snk._snake__snake_speed)

    def fill(self):
        self.__dis.fill(self.__black)

#################################################################################################3

class snake():

    __snake_block = 0
    __snake_speed = 0
    __snake_list = []
    __snake_length = 0
    __x1 = 0
    __y1 = 0
    __origin = []
    __x1_change = 0
    __y1_change = 0

    def __init__(self, brd):
        self.__snake_block = 10
        self.__snake_speed = 15
        self.__snake_length = 1
        self.__x1 = brd._board__dis_width / 2
        self.__y1 = brd._board__dis_height / 2
        self.__origin = [self.__y1, self.__y1]
        self.__x1_change = 0
        self.__y1_change = 0
        self.__snake_list = []

    def restart(self):
        self.__snake_length = 1
        self.__x1 = self.__origin[0]
        self.__y1 = self.__origin[1]
        self.__x1_change = 0
        self.__y1_change = 0
        self.__snake_list = []

    def change_direction(self, direction):

        # 0 - up, 1 - right, 2 - down, 3 - left

        if direction == 0:
            self.__x1_change = 0
            self.__y1_change = -self.__snake_block
        elif direction == 1:
            self.__x1_change = self.__snake_block
            self.__y1_change = 0
        elif direction == 2:
            self.__x1_change = 0
            self.__y1_change = self.__snake_block
        elif direction == 3:
            self.__x1_change = -self.__snake_block
            self.__y1_change = 0
        else:
            self.__x1_change = 0
            self.__y1_change = 0

    def crashed_boundaries(self, brd):
        if self.__x1 >= brd._board__dis_width or self.__x1 < 0 or self.__y1 >= brd._board__dis_height or self.__y1 < 0:
            return True
        else:
            return False

    def move(self):
        self.__x1 += self.__x1_change
        self.__y1 += self.__y1_change

    def crashed_itself(self):
        snake_Head = []
        snake_Head.append(self.__x1)
        snake_Head.append(self.__y1)
        self.__snake_list.append(snake_Head)
        if len(self.__snake_list) > self.__snake_length:
            del self.__snake_list[0]

        for x in self.__snake_list[:-1]:
            if x == snake_Head:
                return True

    def ate(self, brd, fd):
        if self.__x1 == fd._food__foodx and self.__y1 == fd._food__foody:
            fd._food__foodx = round(random.randrange(0, brd._board__dis_width - self.__snake_block) / 10.0) * 10.0
            fd._food__foody = round(random.randrange(0, brd._board__dis_height - self.__snake_block) / 10.0) * 10.0
            self.__snake_length += 1

#################################################################################################3

class food():

    __foodx = 0
    __foody = 0

    def __init__(self, brd, snk):
        self.__foodx = round(random.randrange(0, brd._board__dis_width - snk._snake__snake_block) / 10.0) * 10.0
        self.__foody = round(random.randrange(0, brd._board__dis_height - snk._snake__snake_block) / 10.0) * 10.0

    def restart(self, brd, snk):
        self.__init__(brd, snk)