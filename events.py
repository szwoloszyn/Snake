import pygame
import sys

from settings import *
from mysnake import MySnake, Direction
from apple import Apple

def check_events(screen, snake, apple):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
          check_keydown(event, screen, snake, apple)

def check_keydown(event, screen, snake : MySnake, apple : Apple):
    if event.key == pygame.K_w:
        if snake.direction != Direction.DOWN:
            snake.change_dir(Direction.UP)
    elif event.key == pygame.K_s:
        if snake.direction != Direction.UP:
            snake.change_dir(Direction.DOWN)
    elif event.key == pygame.K_a:
        if snake.direction != Direction.RIGHT:
            snake.change_dir(Direction.LEFT)
    elif event.key == pygame.K_d:
        if snake.direction != Direction.LEFT:
            snake.change_dir(Direction.RIGHT)
    elif event.key == pygame.K_SPACE:
        snake.isEaten = True

def check_collision(screen, snake : MySnake, apple : Apple):
    sets = Settings()
    if snake.get_pos() == apple.get_pos():
        apple.eaten(sets)
        snake.isEaten = True


def foo():
    print("A")