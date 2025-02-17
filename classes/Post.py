import pygame

from constants import *
from helpers import screen
from Comment import Comment


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comment_display_index = 0

    def add_like(self):
        self.likes_counter += 1

    def add_comments(self, text):
        self.comments.append(Comment(text))

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """

        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        # here leave it like that and override it in ImagePost and TextPost
        # screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        # scrren = pygame.display.set_mode(screen_size)
        # img = pygame.image.load('images/background.png')
        # img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        # screen.blit(img, POST_X_POS, POST_Y_POS)
        pass

    def display_header(self):
        # display username and location
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        text = font.render(self.username, True, BLACK)
        screen.blit(text, [USER_NAME_X_POS, USER_NAME_Y_POS])

        # same for location description

    def display_likes(self):
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        text = font.render("Liked by " + str(self.likes_counter) + " users", True, BLACK)
        screen.blit(text, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])
        #font1 = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        # text1 = font.render(str('500'), True, BLACK)
        # screen.blit(text1, [SHARE_BUTTON_X_POST, SHARE_BUTTON_Y_POS])

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        """
                Display comments on post. In case there are more than 4
                comments, show only 4 comments chosen by reset_comments_display_index

                :return: None
                """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
    def view_more_comments(self):
        pass

