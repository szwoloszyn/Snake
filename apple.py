import pygame
import random
import copy

from settings import *
from mysnake import MySnake, Direction

class Apple():
    """class representing food for snake"""
    def __init__(self, sets : Settings):
        """cords randomly chosen in my screen edges (*GAP) so they spawn in my frames"""
        self.size = sets.gap
        GAP = sets.gap
        self.x = (random.randint( int(sets.leftEdge/GAP),int((sets.rightEdge-GAP)/GAP) ))*GAP
        self.y = (random.randint( int(sets.upperEdge/GAP),int((sets.lowerEdge-GAP)/GAP) ))*GAP
        self.color = (255,0,0)

    def get_pos(self):
        return (self.x, self.y)
    
    def deep_copy(self):
        """deep copy so I can actually copy the segments for moving them"""
        return copy.deepcopy(self)
    
    def eaten(self,sets : Settings):
        """changes position of an apple when it got eaten"""
        GAP = sets.gap
        self.x = (random.randint( int(sets.leftEdge/GAP),int((sets.rightEdge-GAP)/GAP) ))*GAP
        self.y = (random.randint( int(sets.upperEdge/GAP),int((sets.lowerEdge-GAP)/GAP) ))*GAP
    def drawme(self, screen):
        """prints apple on the screen"""
        myRect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect( screen, self.color, myRect)
        
    def update(self, screen):
        self.drawme(screen)
