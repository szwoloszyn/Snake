import pygame.font
from settings import *

pygame.font.init()

class Menu():
    def __init__(self, screen, sets):
        self.playing = True
        self.reset = False
        self.score = 0
        self.playButton = Button(screen, sets, "PLAY AGAIN")
    def play(self):
        if not self.playing:
            self.score = 0
            self.playing = True
    def finish(self):
        if self.playing:
            self.playing = False
    def draw_score(self, screen : pygame.Surface, sets : Settings):
        if self.playing:
            font = pygame.font.SysFont('arial',24)
            capt = "score: " + str(self.score)
            msg = font.render(capt, True, sets.WHITE)
            msg_rect = msg.get_rect()
            msg_rect.left = sets.gap / 2
            msg_rect.top = sets.gap / 2
            screen.blit(msg, msg_rect)
        else:
            font = pygame.font.SysFont('arial',30)
            capt = "SCORE: " + str(self.score)
            msg = font.render(capt, True, sets.WHITE)
            msg_rect = msg.get_rect()
            move = self.playButton.height
            msg_rect.center = self.playButton.myButton.center
            msg_rect.centery -= move
            screen.blit(msg, msg_rect)
            pass


class Button():
    def __init__(self, screen : pygame.Surface, sets : Settings, caption : str):
        self.width = 230
        self.height = 70
        self.screen_rect = screen.get_rect()
        self.myButton = pygame.Rect( 0, 0, self.width, self.height)
        self.myButton.center = self.screen_rect.center
        self.buttonColor = sets.RED
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.msg = self.font.render(caption, True, sets.WHITE)
        self.msg_rect = self.msg.get_rect()
        self.msg_rect.center = self.myButton.center

    def ifCollides(self, x, y):
        if self.myButton.collidepoint(x,y):
            return True
        else:
            return False

    def drawme(self, screen, sets : Settings):
        pygame.draw.rect(screen, self.buttonColor, self.myButton)
        screen.blit(self.msg, self.msg_rect)