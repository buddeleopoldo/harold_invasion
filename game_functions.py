import sys
import pygame
from bullet import Bullet
from girl import Girl
from time import sleep
from button import Button

def check_events(hi_settings, stats, screen, harold, girls, bullets, \
    play_button, sb):
    """ Responds to keyboard and mouse """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(hi_settings, stats, screen, harold, girls, \
                bullets, play_button, mouse_x, mouse_y, sb)

    # Keybord move harold
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hi_settings, screen, harold, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hi_settings, screen, harold, bullets)


def check_play_button(hi_settings, stats, screen, harold, girls, bullets, \
    play_button, mouse_x, mouse_y, sb):
    """ Starts new game when player clicks play """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset game settings
        hi_settings.initialize_dynamic_settings()

        # Hide mouse click
        pygame.mouse.set_visible(False)

        # Reset stats
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score(hi_settings.bg_color)
        sb.prep_level(hi_settings.bg_color)
        sb.prep_harolds(hi_settings.bg_color)

        # Empty girls and bullets
        girls.empty()
        bullets.empty()

        # Create new fleet and center harold
        create_fleet(hi_settings, screen, harold, girls)
        harold.center_harold()


def check_keydown_events(event, hi_settings, screen, harold, bullets):
    """ Handles key presses """
    # Quit
    if event.key == pygame.K_q:
        sys.exit()
    # Moving
    if event.key == pygame.K_RIGHT:
        harold.moving_right = True
        hi_settings.right_flag = True
    elif  event.key == pygame.K_LEFT:
        harold.moving_left = True
        hi_settings.left_flag = True
    # Accelerate moving "A"
    elif  event.key == pygame.K_a:
        harold.hi_settings.harold_speed_factor = \
            harold.hi_settings.harold_speed_factor * 3
    # Accelerate shots "S"
    elif  event.key == pygame.K_s:
        for bullet in bullets:
            bullet.speed_factor = hi_settings.bullet_speed_factor * 8
    # Shot "SPACE"
    elif  event.key == pygame.K_SPACE:
        fire_bullet(hi_settings, screen, harold, bullets)
    # Shot "SPACE"
    if event.key == pygame.K_UP:
        hi_settings.up_flag = True


def fire_bullet(hi_settings, screen, harold, bullets):
    # create bullet and add it to group
    if len(bullets) < hi_settings.bullets_allowed:
        new_bullet = Bullet(hi_settings, screen, harold)
        bullets.add(new_bullet)


def check_keyup_events(event, hi_settings, screen, harold, bullets):
    """ Handles key releases """
    # Moving
    if event.key == pygame.K_RIGHT:
        harold.moving_right = False
        hi_settings.right_flag = False
    elif  event.key == pygame.K_LEFT:
        harold.moving_left = False
        hi_settings.left_flag = False
    # Original moving
    elif  event.key == pygame.K_a:
        harold.hi_settings.harold_speed_factor = \
            harold.hi_settings.harold_speed_factor / 3
    if event.key == pygame.K_UP:
        hi_settings.up_flag = False


def update_screen(hi_settings, stats, screen, harold, girls, bullets, \
    play_button, sb):
        # Redraw the screen during each pass through the loop.
        hi_settings.bg_color[0] = int(hi_settings.color_temp)
        screen.fill(hi_settings.bg_color)
        hi_settings.color_up, hi_settings.color_temp = \
            var_color(hi_settings.color_up, hi_settings.color_temp)
        harold.blitme()
        girls.draw(screen)

        # Redraw bullets bihind harold and aliens
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        # Draw play button
        if not stats.game_active:
            play_button.draw_button()

        # Show scoreboard
        sb.show_score(hi_settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


def var_color(color_up, color_temp):
    """ Variates a number between 1 and 254 at different speeds """
    if color_up:
        color_temp += 0.5
        if int(color_temp) == 254:
            color_up = False
    else:
        color_temp -= 0.8
        if int(color_temp) == 1:
            color_up = True

    return color_up, color_temp


def update_bullets(hi_settings, stats, screen, harold, girls, bullets, sb):
    """ Update bullet position and get rid of old ones """
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Both on, bullet MrBean stays and Harold changes
    if hi_settings.left_flag and hi_settings.right_flag:
        for bullet in bullets:
            bullet.image = pygame.image.load('images/mr_bean.bmp')
            bullet.speed_factor = hi_settings.bullet_speed_factor * 0.3
        harold.image = pygame.image.load('images/bean_shot.bmp')

    # Check for collisions
    check_bullet_girl_collisions(hi_settings, stats, screen, harold, girls, \
        bullets, sb)


def check_bullet_girl_collisions(hi_settings, stats, screen, harold, girls, \
    bullets, sb):
    """ Respond to collisions """
    # Check for colisions, get rid of bullet and girl
    if hi_settings.left_flag and hi_settings.right_flag:
        # Both on, bullet MrBean stays and Harold changes
        collisions = pygame.sprite.groupcollide(bullets, girls, False, True)
    else:
        collisions = pygame.sprite.groupcollide(bullets, girls, True, True)

    if collisions:
        for girls in collisions.values():
            stats.score += hi_settings.girl_points * len(girls)
            sb.prep_score()
        check_high_score(hi_settings, stats, sb)

    # Check if all girls were distroyed
    if len(girls) == 0:
        # Destroy bullets and create new fleet
        bullets.empty()
        hi_settings.increase_speed()
        create_fleet(hi_settings, screen, harold, girls)
        # Starts new level
        stats.level += 1
        sb.prep_level(hi_settings.bg_color)


def create_fleet(hi_settings, screen, harold, girls):
    """ Creates a fleet of girls """
    girl = Girl(hi_settings, screen)
    number_girls_x = get_number_girls_x(hi_settings, girl.rect.width)
    number_rows = get_number_rows(hi_settings, harold.rect.height, \
        girl.rect.height)

    # Create fleet
    for row_number in range(number_rows):
        for girl_number in range(number_girls_x):
            # Create girl and place it in the row
            create_girl(hi_settings, screen, girls, girl_number, row_number)


def get_number_girls_x(hi_settings, girl_width):
    """ Find number of girls in a row """
    available_space_x = hi_settings.screen_width - 2*girl_width
    number_girls_x = int(available_space_x / (2*girl_width))
    return number_girls_x


def get_number_rows(hi_settings, harold_height, girl_height):
    """ Determine girls rows to fit on screen """
    available_space_y = hi_settings.screen_height - 2*girl_height - harold_height
    number_rows = int(available_space_y / (2*girl_height))
    return number_rows


def create_girl(hi_settings, screen, girls, girl_number, row_number):
    girl = Girl(hi_settings, screen)
    girl_width = girl.rect.width
    girl_height = girl.rect.height
    girl.x = 0.5*girl_width + 2 * girl_width * girl_number
    girl.rect.x = girl.x
    girl.rect.y = 0.5*girl_height + 1.7 * girl_height * row_number
    girls.add(girl)


def update_girls(hi_settings, stats, screen, harold, girls, bullets, sb):
    """ If the fleet is at an edge, move down and change dir """
    check_fleet_edges(hi_settings, girls)
    girls.update()

    # Look for collision with harold
    if pygame.sprite.spritecollideany(harold, girls):
        print("Poor Harold!!!")
        harold_hit(hi_settings, stats, screen, harold, girls, bullets, sb)

    # Look for girls hitting the bottom
    check_girl_bottom(hi_settings, stats, screen, harold, girls, bullets, sb)


def check_fleet_edges(hi_settings, girls):
    """ Check if reached an edge and change dir """
    for girl in girls.sprites():
        if girl.check_edges():
            change_fleet_direction(hi_settings, girls)
            break


def change_fleet_direction(hi_settings, girls):
    """ Drop and change direction """
    for girl in girls.sprites():
        girl.rect.y += hi_settings.fleet_drop_speed
    hi_settings.fleet_direction *= -1


def check_girl_bottom(hi_settings, stats, screen, harold, girls, bullets, sb):
    """ Checks if a girl reaches the bottom of the screen """
    screen_rect = screen.get_rect()
    for girl in girls.sprites():
        if girl.rect.bottom >= screen_rect.bottom:
            # Do the same that bullet hits harold
            harold_hit(hi_settings, stats, screen, harold, girls, bullets, sb)
            break


def harold_hit(hi_settings, stats, screen, harold, girls, bullets, sb):
    """ Respond to harold hit by girl """
    if stats.harold_left > 0:
        # Decrement HAROLDS left
        stats.harold_left -= 1
        sb.prep_harolds(hi_settings.bg_color)

        # Empty girls and bullets
        girls.empty()
        bullets.empty()

        # Create new fleet and center the ship
        create_fleet(hi_settings, screen, harold, girls)
        harold.center_harold()

        # Pause
        sleep(1)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(hi_settings, stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score(hi_settings.bg_color)