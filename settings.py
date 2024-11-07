from enum import Enum
direction = {
    'LEFT' : 0,
    'UP' : 1,
    'RIGHT' : 2,
    'DOWN' : 3
}

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class Settings:
    def __init__(self):
        self.screen_width = 707
        self.screen_height = 351
        self.bg_color = (138,219,118)

        self.gap = 16
        self.zeit = 0.025