import pygame
import sys, time

from settings import *
from mysnake import MySnake, Direction
from apple import Apple

def check_events(screen, snake, apple):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
          check_keydown(event, screen, snake, apple)
          break

def check_keydown(event, screen, snake : MySnake, apple : Apple):
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        if snake.direction != Direction.DOWN:
            snake.change_dir(Direction.UP)
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        if snake.direction != Direction.UP:
            snake.change_dir(Direction.DOWN)
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        if snake.direction != Direction.RIGHT:
            snake.change_dir(Direction.LEFT)
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        if snake.direction != Direction.LEFT:
            snake.change_dir(Direction.RIGHT)
    elif event.key == pygame.K_SPACE:
        snake.isEaten = True

def check_collision(screen, snake : MySnake, apple : Apple):
    sets = Settings()
    if snake.get_pos() == apple.get_pos():
        apple.eaten(sets)
        snake.isEaten = True
    """"prototype of game over - going to endless loop and making endless lag"""
    check = False
    for seg in snake.body[1:]:
        if snake.x == seg.x and snake.y == seg.y:
            game_over()
    
def game_over():
    time.sleep(0.3)
    pygame.quit()
    sys.exit()