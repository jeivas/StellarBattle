import pygame


class Settings:
    def __init__(self):
        # Game settings
        self.fps = 60
        self.screen_width = 1280
        self.screen_height = 720
        self.rgb = (14, 19, 41)
        self.ship_speed = 5

        # Set a limit for the ship movement based on a percentage of the screen.
        self.max_movement_width = self.screen_width * 0.97
        self.min_movement_height = self.screen_height * 0.6
        self.max_movement_height = self.screen_height * 0.91

        # Bullet Settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (135, 206, 235)
        self.bullet_max = 5

        # Alien settings
        self.alien_speed = 2
        self.alien_max_deep = 650
        self.aliens_max = 3

        # Points settings
        self.font = pygame.font.SysFont("Impact", 32)
        self.font_border_color = pygame.Color(255, 0, 0)
        self.font_color = pygame.Color(255, 255, 255)
        self.points_position = (1235, 25)
