import pygame

from settings import *
from mysnake import MySnake, Direction
import events
from apple import Apple


def draw_screen(screen, sets : Settings):
    edges = sets.get_screen_edges()
    for x in edges:
        pygame.draw.line(screen ,x[0],x[1],x[2])
        #pygame.draw.line(screen ,x)

def run():
    pygame.init()
    sets = Settings()
    screen = pygame.display.set_mode( (sets.screen_width,sets.screen_height) )
    pygame.display.set_caption("SNAKE")
    screen.fill(sets.bg_color)
    apple = Apple(sets)
    snake = MySnake(sets)
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(sets.bg_color)
        draw_screen(screen, sets)
        apple.update(screen)
        snake.update(screen)
        events.check_events(screen, snake, apple)
        events.check_collision(screen, snake, apple)
        
        pygame.display.flip()
        clock.tick(sets.maxfps)
        
run()
