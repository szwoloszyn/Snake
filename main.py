import pygame

from settings import *
from mysnake import MySnake, Direction
import events
from apple import Apple

def run():
    pygame.init()
    sets = Settings()
    screen = pygame.display.set_mode( (sets.screen_width,sets.screen_height) )
    pygame.display.set_caption("SNAKE")
    screen.fill(sets.bg_color)
    apple = Apple(sets)
    snake = MySnake(sets)
    clock = pygame.time.Clock()

# zmiany FPS do zrobienia...

    while True:
        screen.fill(sets.bg_color)
        apple.update(screen)
        snake.update(screen)
        events.check_events(screen, snake, apple)
        events.check_collision(screen, snake, apple)
        
        pygame.display.flip()
        clock.tick(sets.maxfps)
        
run()
