import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, sb_game):
        super().__init__()
        # Initialize screen and screen rect.
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen.get_rect()

        self.settings = sb_game.settings

        # Initialize bullet.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_color = self.settings.bullet_color
        # Position the bullet at the midtop of the ship.
        self.rect.midtop = sb_game.ship.rect.midtop

        self.x = 0
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        self.remove_bullet()

    def draw_bullet(self):
        """Draw the bullet in its current position."""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

    def remove_bullet(self):
        if self.rect.bottom < 0:
            self.kill()
