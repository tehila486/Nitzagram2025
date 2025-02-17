import pygame

from constants import *
from helpers import *
from Post import Post

# done :)
class TextPost(Post):

    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text = from_text_to_array(text) # list
        self.text_color = text_color
        self.background_color = background_color

    def display_content(self):
        background = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, background)
        # go over the list and display all the text
        for i in range (0, len(self.text)):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text[i], True, self.text_color)
            screen.bilt(text,center_text(len(self.text), text, i))
