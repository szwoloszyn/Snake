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
        self.body = [ Segment(self.x,self.y,sets.gap,self.direction) ]
        self.size = len(self.body) 
        self.rect_size = (sets.gap,sets.gap*self.size)
        self.isEaten = False
        self.c = 0
        

    def get_pos(self):
        return (self.x, self.y)

    def eat(self, seg : Segment):
        self.body.append(seg)
        # for seg in self.body:
        #     print(seg.x , " , ",seg.y)
        # print("---------")


    def change_dir(self, dir : Direction):
            self.direction = dir
            self.body[0].direction = dir

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
        return
    
    def move_upt(self):
        sets = Settings()
        zeit = sets.zeit
        time.sleep(zeit)
        copy = []
        for seg in self.body:
            copy.append( seg.deep_copy() )

        if self.direction == Direction.RIGHT:
            self.x += self.rect_size[0]

        elif self.direction == Direction.LEFT:
            self.x -= self.rect_size[0]

        elif self.direction == Direction.UP:
            self.y -= self.rect_size[0]

        elif self.direction == Direction.DOWN:
            self.y += self.rect_size[0]

        if self.y >= sets.screen_height:
            self.y = sets.gap
        if self.x >= sets.screen_width:
            self.x = sets.gap
        if self.y < 0:
            self.y = sets.screen_height - (sets.screen_height%sets.gap)
        if self.x < 0:
            self.x = sets.screen_width - (sets.screen_width%sets.gap)

        self.body[0].x = self.x
        self.body[0].y = self.y
        time.sleep(zeit)
        i = 1
        while i < len(self.body):
            self.body[i] = copy[i-1]
            i += 1
        time.sleep(zeit)
        if self.isEaten:
            self.eat(copy[-1])
            self.isEaten = False
        #return copy[-1]

    def drawme(self, screen):
        #myRect = pygame.Rect(self.x, self.y,
        # self.rect_size[0], self.rect_size[1] )
        #pygame.draw.rect(screen, (20,20,20), myRect )
        for seg in self.body:
            seg.drawme(screen,self.sets)
    
    def update(self, screen):
        #print("SNAKE: (", self.x, " , " , self.y , ")" )
        self.move_upt()
        self.drawme(screen)


        
    