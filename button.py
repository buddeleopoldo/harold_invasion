import pygame.font

class Button():
    """ Creates button """
    def __init__(self, hi_settings, screen, msg):
        """ Initializes button """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimensions and properties
        #self.width, self.height = 200, 50
        self.width, self.height = 400, 80
        #self.button_color = (0, 250, 50)
        self.button_color = (150, 220, 190)
        self.text_color = (100, 0, 240)
        self.text_color = (20, 20, 20)
        self.font = pygame.font.SysFont(None,48)

        # Build rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Buttonmsg prepped once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Turns msg to an image, put it in center of button """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image = pygame.image.load('./images/manual.png')
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw button and then message """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)