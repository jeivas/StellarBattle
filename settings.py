class Settings:
    def __init__(self):
        # Game settings
        self.fps = 60
        self.screen_width = 1280
        self.screen_height = 720
        self.rgb = (14, 19, 41)
        self.ship_speed = 3

        # Set a limit for the ship movement based on a percentage of the screen.
        self.max_movement_width = self.screen_width * 0.97
        self.min_movement_height = self.screen_height * 0.6
        self.max_movement_height = self.screen_height * 0.91

        # Bullet Settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (135, 206, 235)
