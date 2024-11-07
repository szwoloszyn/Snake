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
        snake.direction = Direction.UP
    elif event.key == pygame.K_s:
        snake.direction = Direction.DOWN
    elif event.key == pygame.K_a:
        snake.direction = Direction.LEFT
    elif event.key == pygame.K_d:
        snake.direction = Direction.RIGHT

def check_collision(screen, snake : MySnake, apple : Apple):
    sets = Settings()
    if snake.get_pos() == apple.get_pos():
        apple.eaten(sets)


def foo():
    print("A")