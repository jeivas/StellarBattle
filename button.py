import pygame
from pygame.sprite import Sprite


class Button(Sprite):
    """Class to control the play and play again buttons"""
    def __init__(self, sb_game):
        super().__init__()
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen.get_rect()
        self.settings = sb_game.settings

        # Create the button surface
        self.button_surface = pygame.Surface((150, 50))

        # Setup text for the button
        self.text = sb_game.settings.font.render(self.settings.button_message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.button_surface.get_width() / 2, self.button_surface.get_height() / 2))

        # Create a pygame.Rect object that represents the button's boundaries
        self.button_rect = pygame.Rect(self.screen_rect.x, self.screen_rect.y / 2, 150, 50)

        self.button_rect.center = self.screen_rect.center

    def update(self):
        """Display the button in the center of screen and add hover effects"""
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(self.button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(self.button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(self.button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(self.button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        # Show the button text inside it
        self.button_surface.blit(self.text, self.text_rect)

        # Draw the button on the screen
        self.screen.blit(self.button_surface, (self.button_rect.x, self.button_rect.y))

    def delete_button(self):
        self.kill()
