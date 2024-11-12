import pygame

from settings import *
from mysnake import MySnake, Direction
import events
from apple import Apple
from menu import Menu



### TODO SCORE, STARTING SCREEN, ENDSCREEN ! #
def run():
    pygame.init()
    sets = Settings()
    screen = pygame.display.set_mode( (sets.screen_width,sets.screen_height) )
    pygame.display.set_caption("SNAKE")
    snake_org, apple_org = MySnake(sets) , Apple(sets)
    menu = Menu(screen, sets)
    apple = Apple(sets)
    snake = MySnake(sets)
    clock = pygame.time.Clock()
    print( type(screen))
    while True:
        clock.tick(sets.maxfps)
        if not menu.playing:
            events.update_pause_screen(screen, sets, snake, apple, menu)
            events.check_events(screen, snake, apple, menu)
        else: 
            events.update_playing_screen(screen, sets, snake, apple, menu)
            events.check_events(screen, snake, apple, menu)
            events.check_collision(screen, snake, apple, menu)
        if menu.reset == True:
            snake = snake_org.deep_copy()
            apple = apple_org.deep_copy()
            menu.reset = False

run()
