import pygame
from pygame.sprite import Sprite

class Girl(Sprite):
    """ Represents a single girl """

    def __init__(self, hi_settings, screen):
        """ Initializaes girl and sets initial position """
        super(Girl, self).__init__()
        self.screen = screen
        self.hi_settings = hi_settings

        # Loads image and its rect attribute
        self.image = pygame.image.load('./images/girl.bmp')
        self.rect = self.image.get_rect()

        # Starts each new girl in top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height - 80

        #Stores girl's exact position
        self.x = float(self.rect.x)

    # def blitme(self):
    #     """ Draws girl and current location """
    #     self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ True if girl reaches the edge """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Move the girl right """
        self.x += (self.hi_settings.girl_speed_factor * \
            self.hi_settings.fleet_direction)
        self.rect.x = self.x
