class GameStats():
    """ Track statistics for harold """

    def __init__(self, hi_settings):
        """ Initializes statistics """
        self.hi_settings = hi_settings
        self.reset_stats()
        # Start in inactive state
        self.game_active = False
        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """ Initializes stats that can change inthe game """
        self.harold_left = self.hi_settings.harold_limit
        self.score = 0
        self.level = 1
