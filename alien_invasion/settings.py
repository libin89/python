class Settings():
    """ save all setting class of game """

    def __init__(self):
        """ initialize game setting """
        # screen setting
        self.screen_width = 480
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship speed factor
        self.ship_speed_factor = 1.5

        # bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15

        # frams per second
        self.frames_per_second = 200
