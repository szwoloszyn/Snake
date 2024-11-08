import pygame
import time
import copy

from settings import *

class Segment():
    def __init__(self,x,y,size, dir : Direction):
        self.x = x
        self.y = y
        self.size = size
        self.direction = dir

    def get_pos(self):
        return (self.x, self.y)
    
    def drawme(self, screen, sets : Settings):
        myRect = pygame.Rect(self.x, self.y, self.size, self.size )
        pygame.draw.rect(screen, (20,20,20), myRect )

    def move(self, x, y, sets : Settings):
        zeit = sets.zeit

    def deep_copy(self):
        return copy.deepcopy(self)