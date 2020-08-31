import pygame
import time
import random
import gameClasses as gc

pygame.init()

display = gc.board()
snake1 = gc.snake(display)
food1 = gc.food(display, snake1)

def gameLoop():
    game_over = False
    game_close = False

    while not game_over:

        while game_close == True:
            display.fill()
            display.message("You Lost! Press R-Restart or Q-Quit")
            display.Your_score(snake1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_over = False
                        game_close = False
                        snake1.restart()
                        food1.restart(display, snake1)
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake1.change_direction(0)
                elif event.key == pygame.K_RIGHT:
                    snake1.change_direction(1)
                elif event.key == pygame.K_DOWN:
                    snake1.change_direction(2)
                elif event.key == pygame.K_LEFT:
                    snake1.change_direction(3)

        game_close1 = snake1.crashed_boundaries(display)
        snake1.move()
        display.fill()
        display.show_food(snake1, food1)
        game_close2 = snake1.crashed_itself()
        game_close = game_close1 or game_close2

        display.show_snake(snake1)
        display.Your_score(snake1)

        pygame.display.update()

        snake1.ate(display, food1)
        display.refresh(snake1)

    pygame.quit()
    quit()

gameLoop()