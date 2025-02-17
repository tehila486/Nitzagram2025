import pygame

from constants import *
from helpers import *
from Post import Post

# doneeeeee :)
class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_index):
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS+comment_index*COMMENT_LINE_HEIGHT))