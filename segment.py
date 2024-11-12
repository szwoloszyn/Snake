import pygame
import time
import copy

from settings import *

class Segment():
    """class representing single segment of my snake's body"""
    def __init__(self,x,y,size, dir : Direction):
        self.x = x
        self.y = y
        self.size = size
        self.direction = dir

    def get_pos(self):
        return (self.x, self.y)
    
    def drawme(self, screen, sets : Settings):
        """prints one segment on the screen"""
        myRect = pygame.Rect(self.x, self.y, self.size, self.size )
        pygame.draw.rect(screen, sets.SNAKE_CLR, myRect )

    def deep_copy(self):
        """deep copy so I can actually copy the segments for moving them"""
        return copy.deepcopy(self)