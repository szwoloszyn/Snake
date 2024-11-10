from enum import Enum

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class Settings:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.screen_width = 707
        self.screen_height = 351
        self.bg_color = (138,219,118)
        self.maxfps = 18
        self.gap = 16
        self.zeit = 0.025

        ### white edges on screen ###
        self.upperEdge = 2*self.gap
        self.leftEdge = 2*self.gap
        self.lowerEdge = self.screen_height - self.screen_height%self.gap - self.gap
        self.rightEdge = self.screen_width - self.screen_width%self.gap - self.gap

    def get_screen_edges(self):
        """for drawing edges of playing field"""
        left_up_corner = (self.leftEdge, self.upperEdge)
        left_down_corner = (self.leftEdge, self.lowerEdge)
        right_down_corner = (self.rightEdge, self.lowerEdge )
        right_up_corner = (self.rightEdge, self.upperEdge)
        edges = (
            ( self.WHITE, left_up_corner, left_down_corner),
            ( self.WHITE, left_down_corner, right_down_corner),
            ( self.WHITE, right_down_corner, right_up_corner),
            ( self.WHITE, right_up_corner, left_up_corner)
        )
        return edges