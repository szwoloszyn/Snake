import pygame
from enum import Enum
import time
import copy

from settings import *
from segment import Segment

class MySnake():
    """snake in its entirety"""
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


    def deep_copy(self):
        """deep copy so I can actually copy the segments for moving them"""
        return copy.deepcopy(self)

    def eat(self, seg : Segment):
        """making snake one segment longer"""
        self.body.append(seg)


    def change_dir(self, dir : Direction):
            self.direction = dir
            self.body[0].direction = dir


    def out_of_screen(self, sets: Settings):
        """defining what happens when snake goes out of screen"""
        if self.y >= sets.lowerEdge:
            self.y = sets.upperEdge
        elif self.x >= sets.rightEdge:
            self.x = sets.leftEdge
        elif self.y < sets.upperEdge:
            self.y = sets.lowerEdge - sets.gap
        elif self.x < sets.leftEdge:
            self.x = sets.rightEdge - sets.gap
        self.body[0].x = self.x
        self.body[0].y = self.y


    def move(self):
        """changing x,y cords of each segment in body every tick"""
        sets = Settings()
        zeit = sets.zeit
        time.sleep(zeit)
## creating deep copy of body so I can move it one segment forward ##
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

        self.out_of_screen(sets)

        #time.sleep(zeit)
        i = 1
        while i < len(self.body):
            self.body[i] = copy[i-1]
            i += 1
        #time.sleep(zeit)
        if self.isEaten:
            self.eat(copy[-1])
            self.isEaten = False


    def drawme(self, screen):
        """prints snake on the screen"""
        for seg in self.body:
            seg.drawme(screen,self.sets)
    
    
    def update(self, screen):
        #print("SNAKE: (", self.x, " , " , self.y , ")" )
        self.move()
        self.drawme(screen)