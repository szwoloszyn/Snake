import pygame
import sys, time

from settings import *
from mysnake import MySnake, Direction
from apple import Apple
from menu import Menu

def draw_screen(screen, sets : Settings):
    """prints screen edges on which game operates"""
    edges = sets.get_screen_edges()
    for x in edges:
        pygame.draw.line(screen ,x[0],x[1],x[2])

def update_playing_screen(screen, sets: Settings, snake : MySnake, apple : Apple, menu : Menu):
        """updates every game piece"""
        screen.fill(sets.bg_color)
        draw_screen(screen, sets)
        apple.update(screen)
        snake.update(screen)
        menu.draw_score(screen, sets)
        pygame.display.flip()

def update_pause_screen(screen, sets: Settings, snake : MySnake, apple : Apple, menu : Menu):
    screen.fill(sets.bg_color)
    draw_screen(screen, sets)
    menu.playButton.drawme(screen, sets)
    menu.draw_score(screen, sets)
    if menu.score != 0:
        menu.draw_score(screen, sets)
        pass

    pygame.display.flip()
    


def check_events(screen, snake : MySnake, apple : Apple, menu : Menu):
    """going through all input events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over(snake, apple, menu)
            pygame.quit()
            sys.exit()
            #if not menu.playing:
                #pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mousedown(event, screen, snake, apple, menu)
            return 
        elif event.type == pygame.KEYDOWN:
          check_keydown(event, screen, snake, apple, menu)
          break


def check_mousedown(event, screen, snake : MySnake, apple : Apple, menu : Menu):
    mouse = pygame.mouse.get_pos()
    if menu.playButton.ifCollides(mouse[0], mouse[1]):
        menu.play()


def check_keydown(event, screen, snake : MySnake, apple : Apple, menu : Menu):
    if event.key == pygame.K_SPACE:
        snake.isEaten = True
        return
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
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


def check_collision(screen, snake : MySnake, apple : Apple, menu : Menu):
    """checks for collisions beetwen my objects. Like snake hits food or hits itself"""
    sets = Settings()
    if snake.get_pos() == apple.get_pos():
        apple.eaten(sets)
        snake.isEaten = True
        menu.score += 1
    for seg in snake.body[1:]:
        if snake.x == seg.x and snake.y == seg.y:
            game_over(snake, apple, menu)
            return

def game_over(snake : MySnake, apple : Apple, menu : Menu):
    """what happens when player loses"""
    menu.reset = True
    menu.finish()
    time.sleep(0.3)
    #pygame.quit()
    #sys.exit()