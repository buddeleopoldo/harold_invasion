import pygame.font
from pygame.sprite import Group
from harold import Harold

class Scoreboard():
    """ Scoring info """
    def __init__(self, hi_settings, screen, stats):
        """ Init attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.hi_settings = hi_settings
        self.stats = stats

        # Font settings
        self.text_color = (200, 200, 255)
        self.font = pygame.font.SysFont(None, 35)

        # Prepare initial score image
        self.prep_score()
        self.prep_high_score(hi_settings.bg_color)
        self.prep_level(hi_settings.bg_color)
        self.prep_harolds(hi_settings.bg_color)

    def prep_score(self):
        """ Turn score into an image """
        score_str = str(self.stats.score)

        rounded_score = int(round(self.stats.score, -1))
        self.score_str = 'SCORE: ' + "{:,}".format(rounded_score)

        self.score_image = self.font.render(self.score_str, True, \
            self.text_color, self.hi_settings.bg_color)

        # Display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self, bg_color):
        """ Turn high score in rendered image """
        high_score = int(round(self.stats.high_score, -1))
        self.high_score_str = 'Highest score: ' + "{:,}".format(high_score)
        self.high_score_image = self.font.render(self.high_score_str, True, \
            self.text_color, bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self, bg_color):
        """ Turn high score in rendered image """
        level = self.stats.level
        self.level_str = 'Level: ' + "{:,}".format(level)
        self.level_image = self.font.render(self.level_str, True, \
            self.text_color, bg_color)

        # Center the high score at the top of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right -20
        self.level_rect.top = 50#self.score_rect.top

    def prep_harolds(self, bg_color):
        """ Show Harolds left """
        self.harolds = Group()
        for harold_number in range(self.stats.harold_left):
            harold = Harold(self.hi_settings, self.screen)
            harold.image = pygame.image.load('images/face.bmp')
            harold.rect.x = 10 + harold_number * 70
            harold.rect.y = 20
            self.harolds.add(harold)

    def show_score(self, bg_color):
        """ Draw score and highest score"""
        self.screen.blit(self.font.render(self.score_str, True, \
            (255,255,255), bg_color), self.score_rect)
        self.screen.blit(self.font.render(self.high_score_str, True, \
            self.text_color, bg_color), self.high_score_rect)
        self.screen.blit(self.font.render(self.level_str, True, \
            (0,255,255), bg_color), self.level_rect)
        self.harolds.draw(self.screen)
