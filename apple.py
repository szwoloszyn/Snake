import pygame
import random

from settings import *
from mysnake import MySnake, Direction

class Apple():
    def __init__(self, sets : Settings):
        self.radius = sets.gap / 2
        GAP = sets.gap
        self.x = (random.randint( 1,int((sets.screen_width-GAP)/GAP) ))*GAP
        self.y = (random.randint( 1,int((sets.screen_height-GAP)/GAP) ))*GAP
        self.color = (255,0,0)

    def get_pos(self):
        return (self.x, self.y)
    
    def eaten(self,sets : Settings):
        GAP = sets.gap
        self.x = (random.randint( 1,int((sets.screen_width-GAP)/GAP) ))*GAP
        self.y = (random.randint( 1,int((sets.screen_height-GAP)/GAP) ))*GAP
        #print("(", self.x, " , " , self.y , ")" )
    def drawme(self, screen):
        #pygame.draw.circle(screen, self.color, 
        #(self.x,self.y), self.radius)
        myRect = pygame.Rect(self.x, self.y, 2*self.radius, 2*self.radius)
        pygame.draw.rect( screen, self.color, myRect)
        

    def update(self, screen):
        #print("APPLE: (", self.x, " , " , self.y , ")" )
        self.drawme(screen)
