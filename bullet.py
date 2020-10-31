import pygame
from pygame.sprite import Sprite

# class Bullet(Sprite):
#     """ Bullet class that inherits from Sprite """
#     def __init__(self, hi_settings, screen, harold):
#         """ Create bullet at harolds posotion """
#         super(Bullet, self).__init__()
#         self.screen = screen

#         # Create bullet at 0,0 and then correct position
#         self.rect = pygame.Rect(0,0, hi_settings.bullet_width,
#             hi_settings.bullet_height)
#         self.rect.centerx = harold.rect.centerx
#         self.rect.top = harold.rect.top
#         # Store bullet position at decimal value
#         self.y = float(self.rect.y)

#         self.color = hi_settings.bullet_color
#         self.speed_factor = hi_settings.bullet_speed_factor

#     def update(self):
#         """ Moving the bullet """
#         self.y -= self.speed_factor
#         self.rect.y = self.y

#     def draw_bullet(self):
#         """ Draw bullet to the screen """
#         pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet(Sprite):
    """ Bullet class that inherits from Sprite """
    def __init__(self, hi_settings, screen, harold):
        """ Create bullet at harolds posotion """
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet at 0,0 and then correct position
        self.image = pygame.image.load('images/angry_man.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = harold.rect.centerx
        self.rect.top = harold.rect.top
        # Store bullet position at decimal value
        self.y = float(self.rect.y)

        self.color = hi_settings.bullet_color
        self.speed_factor = hi_settings.bullet_speed_factor

    def update(self):
        """ Moving the bullet """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw bullet to the screen """
        self.screen.blit(self.image, self.rect)
