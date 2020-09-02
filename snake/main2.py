import pygame
import time
import random
from Food import Food
from Snake import Snake
from Board import Board

pygame.init()

board = Board()
snake = Snake(board.DISPLAY_WIDTH, board.DISPLAY_HEIGHT, board.BLOCK_SIZE)
food = Food(board.DISPLAY_WIDTH, board.DISPLAY_HEIGHT, board.BLOCK_SIZE)

game_over = False
game_close = False

def gameLoop():

    global game_over, game_close
    
    while not game_over:

        while game_close == True:
            board.fill()
            board.message("You Lost! Press R-Restart or Q-Quit")
            board.show_your_score(snake.getLength())
            pygame.display.update()

            checkFinalMenu()

        checkSnakeMovement()

        game_close1 = board.updateBoard(snake,food)
        game_close2 = snake.crashed_itself()
        game_close = game_close1 or game_close2

        snake.move()

        checkIfSnakeEats()

        pygame.display.update()

    pygame.quit()
    quit()

def checkIfSnakeEats():
    global snake
    global food
    if snake.getSnakeHeadPositionX() == food.getPositionX() and snake.getSnakeHeadPositionY() == food.getPositionY():
        food.restart(board.DISPLAY_WIDTH, board.DISPLAY_HEIGHT, board.BLOCK_SIZE)
        snake.increaseLength()

def checkSnakeMovement():
    global snake
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0)
            elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(2)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(3)

def checkFinalMenu():
    global game_over, game_close, snake, food
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_over = True
                game_close = False
            if event.key == pygame.K_r:
                game_over = False
                game_close = False
                snake.restart()
                food.restart(board.DISPLAY_WIDTH, board.DISPLAY_HEIGHT, board.BLOCK_SIZE)
                gameLoop()    

gameLoop()