import pygame

from constants import *
from helpers import screen
from Post import Post

# donedeeeee
class ImagePost(Post):
    def __init__(self, username,location,description, img_src):
        super().__init__(username,location,description)
        image = pygame.image.load(img_src)
        image = pygame.transform.scale(image,(POST_WIDTH,POST_HEIGHT))
        self.image = image
    def display_content(self):#מציג את התמונה
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
