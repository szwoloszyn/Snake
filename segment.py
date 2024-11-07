import pygame
import time

from settings import *

class Segment():
    def __init__(self,x,y,size, dir : Direction):
        self.x = x
        self.y = y
        self.size = size
        self.direction = dir

    def get_pos(self):
        return (self.x, self.y)
    
    def move(self, x, y, sets : Settings):
        zeit = sets.zeit

