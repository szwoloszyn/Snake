import pygame
import sys, time

from settings import *
from mysnake import MySnake, Direction
from apple import Apple

def draw_screen(screen, sets : Settings):
    """prints screen edges on which game operates"""
    edges = sets.get_screen_edges()
    for x in edges:
        pygame.draw.line(screen ,x[0],x[1],x[2])

def update_screen(screen, sets: Settings, snake : MySnake, apple : Apple):
        """updates every game piece"""
        screen.fill(sets.bg_color)
        draw_screen(screen, sets)
        apple.update(screen)
        snake.update(screen)

        pygame.display.flip()


def check_events(screen, snake, apple):
    """going through all input events"""
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
    """checks for collisions beetwen my objects. Like snake hits food or hits itself"""
    sets = Settings()
    if snake.get_pos() == apple.get_pos():
        apple.eaten(sets)
        snake.isEaten = True
    #prototype of game over - going to endless loop and making endless lag
    for seg in snake.body[1:]:
        if snake.x == seg.x and snake.y == seg.y:
            game_over()


def game_over():
    """what happens when player loses"""
    time.sleep(0.3)
    pygame.quit()
    sys.exit()