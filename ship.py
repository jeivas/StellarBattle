import pygame.image


class Ship:
    """"Class to manage the ship"""

    def __init__(self, sb_game):
        """"Initialize and manage the ship's position"""
        # Initialize screen and screen rect
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen.get_rect()

        # Loads the image and reduce its size
        self.image = pygame.image.load("assets/images/shipImg.bmp")
        self.rect = self.image.get_rect()
        pygame.display.set_icon(self.image)

        # Sets the position of the ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_me(self):
        """"Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)

