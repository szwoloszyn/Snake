import pygame
from enum import Enum
import time

from settings import *
from segment import Segment

class MySnake():
    def __init__(self, sets : Settings):
        self.sets = sets

        x_add = (sets.screen_width/2)%sets.gap
        y_add = (sets.screen_height/2)%sets.gap
        self.x = ( sets.screen_width / 2 ) - x_add
        self.y = ( sets.screen_height / 2 ) - y_add

        self.direction =  Direction.RIGHT
        self.body = [Segment(self.x,self.y,sets.gap,self.direction)]
        self.size = len(self.body) 
        self.rect_size = (sets.gap,sets.gap*self.size)
        
        

    def get_pos(self):
        return (self.x, self.y)

    def move(self):
        sets = Settings()
        zeit = sets.zeit
        time.sleep(zeit)
        if self.direction == Direction.RIGHT:
            time.sleep(zeit)
            self.x += self.rect_size[0]
            time.sleep(zeit)
        elif self.direction == Direction.LEFT:
            time.sleep(zeit)
            self.x -= self.rect_size[0]
            time.sleep(zeit)
        elif self.direction == Direction.UP:
            time.sleep(zeit)
            self.y -= self.rect_size[0]
            time.sleep(zeit)
        elif self.direction == Direction.DOWN:
            time.sleep(zeit)
            self.y += self.rect_size[0]
            time.sleep(zeit)

        if self.y >= sets.screen_height:
            self.y = sets.gap
        if self.x >= sets.screen_width:
            self.x = sets.gap
        if self.y < 0:
            self.y = sets.screen_height - (sets.screen_height%sets.gap)
        if self.x < 0:
            self.x = sets.screen_width - (sets.screen_width%sets.gap)
        return
    
    def drawme(self, screen):
        #screen.fill(self.sets.bg_color)
        myRect = pygame.Rect(self.x, self.y,self.rect_size[0], self.rect_size[1] )
        #myRect = pygame.Rect( self.size, self.size,self.x, self.y )
        pygame.draw.rect(screen, (20,20,20), myRect )

    def update(self, screen):
        #print("SNAKE: (", self.x, " , " , self.y , ")" )
        self.move()
        self.drawme(screen)


        
    