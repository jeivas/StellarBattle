import random

import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, sb_game):
        super().__init__()
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen.get_rect()
        self.settings = sb_game.settings

        self.alien_image = pygame.image.load("assets/images/Nave.png.")
        self.rect = self.alien_image.get_rect()

        self.rect.y = random.randint(-500, 0)

        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.y = float(self.rect.y)

    def blit_me(self):
        """Show alien in its current position on screen"""
        self.screen.blit(self.alien_image, self.rect)

    def update(self):
        """Update aliens y position"""
        self.y += self.settings.alien_speed

        self.rect.y = self.y
