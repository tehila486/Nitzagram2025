import pygame

from constants import *
from helpers import screen
from Post import Post


class TextPost(Post):
    def __init__(self,text, text_color, background_color):
        self.text= text
        self.text_color=text_color
        self.background_color= background_color

    def display(self):
        background = pygame.Rect(POST_WIDTH, POST_HEIGHT, POST_X_POS, POST_Y_POS)
        pygame.draw.rect(screen, self.background_color, background)
