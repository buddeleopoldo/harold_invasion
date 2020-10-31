import pygame
import game_functions as gf
from settings import Settings
from harold import Harold
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # initialize game, create screen object
    pygame.init()
    hi_settings = Settings()
    screen = pygame.display.set_mode((hi_settings.screen_width, hi_settings.screen_height))
    pygame.display.set_caption('Harlod Invasion')

    # Create Herold, group of bullets, group of girls, fleet, stats, button, sb
    harold = Harold(hi_settings, screen)
    bullets = Group()
    girls = Group()
    gf.create_fleet(hi_settings, screen, harold, girls)
    stats = GameStats(hi_settings)
    play_button = Button(hi_settings, screen, "PLAY")
    sb = Scoreboard(hi_settings, screen, stats)

    # Start the main loop for the game
    while True:
        gf.check_events(hi_settings, stats, screen, harold, girls, bullets, \
            play_button, sb)

        if stats.game_active:
            harold.update()
            gf.update_bullets(hi_settings, stats, screen, harold, girls, bullets, sb)
            gf.update_girls(hi_settings, stats, screen, harold, girls, bullets, sb)

        gf.update_screen(hi_settings, stats, screen, harold, girls, bullets, \
            play_button, sb)

run_game()