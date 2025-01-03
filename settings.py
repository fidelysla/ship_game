
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 4.2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.5
        self.bullet_width = 3.4
        self.bullet_height = 14

        # self.bullet_color = (60, 60, 60)
        self.bullet_color = (141, 11, 65)
        self.bullet_allowed = 16

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 40
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
