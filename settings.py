class Settings():
    """ Unifies the settings of the game """

    def __init__(self):
        """ Initializes game static settings """

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self. bg_color = [20, 20, 50]
        self.color_up = True
        self.color_temp = 0

        # Harold settings
        self.harold_speed_factor = 2
        self.harold_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 250, 250, 250
        self.bullets_allowed = 5
        self.left_flag = False
        self.right_flag = False

        # Girl settings
        self.girl_speed_factor = 0.5
        self.fleet_drop_speed = 20#5

        # How quick game and point value speeds up
        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initializes changing settings """
        self.harold_speed_factor = 2
        self.bullet_speed_factor = 3
        self.girl_speed_factor = 2

        # 1 means right, -1 means left
        self.fleet_direction = 1

        # Scoring
        self.girl_points = 50

    def increase_speed(self):
        """ Increase speed and point settings """
        self.harold_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.girl_speed_factor *= self.speedup_scale
        self.girl_points = int(self.girl_points * self.score_scale)
        print(self.girl_points)
