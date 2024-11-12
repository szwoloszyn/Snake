from enum import Enum

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class Settings:
    def __init__(self):
        ### COLORS SET 1
        self.ED_N_CAP_CLR = (255, 255, 255) # edges and captions
        self.APPLE_CLR = (255, 50, 50)
        self.bg_color = (138,219,118)
        self.SNAKE_CLR = (10, 10, 10)
        ### COLOR SET 2
        self.ED_N_CAP_CLR = (255, 255, 255) # edges and captions
        self.APPLE_CLR = (255, 255, 255)
        self.bg_color = (0,0,0)
        self.SNAKE_CLR = (0, 250, 20)
        ### REST SETTINGS
        self.screen_width = 707
        self.screen_height = 351
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
            ( self.ED_N_CAP_CLR, left_up_corner, left_down_corner),
            ( self.ED_N_CAP_CLR, left_down_corner, right_down_corner),
            ( self.ED_N_CAP_CLR, right_down_corner, right_up_corner),
            ( self.ED_N_CAP_CLR, right_up_corner, left_up_corner)
        )
        return edges