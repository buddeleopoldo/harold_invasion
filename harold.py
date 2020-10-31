import pygame
from pygame.sprite import Sprite


class Harold(Sprite):

    def __init__(self, hi_settings, screen):
        """ Initialize harold and set its starting position """
        super(Harold, self).__init__()
        self.screen = screen
        self.hi_settings = hi_settings
        # Load the harold image and get its rect
        self.image = pygame.image.load('images/harold.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new harold at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store decimal value for the harold center
        self.center = float(self.rect.centerx)
        # Movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update harold position according to movement """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load('images/harold_shoot.bmp')
            self.center += self.hi_settings.harold_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.image = pygame.image.load('images/harold_shoot.bmp')
            self.center -= self.hi_settings.harold_speed_factor
        else:
            self.image = pygame.image.load('images/harold.bmp')
        self.rect.centerx = self.center

    def blitme(self):
        """ Draw the harold at its current location """
        self.screen.blit(self.image, self.rect)

    def center_harold(self):
        """ Center harold when hit by girl """
        self.center = self.screen_rect.centerx
