import pygame.image


class Ship:
    """Class to manage ship's behavior and resources."""

    def __init__(self, sb_game):
        """Initialize and manage the ship's position."""
        # Initialize screen and screen rect.
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen.get_rect()

        # Loads the image of the ship
        self.image = pygame.image.load("assets/images/shipImg.bmp.")
        self.rect = self.image.get_rect()
        pygame.display.set_icon(self.image)

        # Sets the position of the ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag (controls if the ship moves or not). False: Ship doesn't move;
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Store the float value of the rect
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.settings = sb_game.settings

    def blit_me(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

    def update_ship_position(self):
        """Update rect position if the flag attribute is true"""
        # Set a limit for the ship movement based on a percentage of the screen.
        max_width = self.settings.screen_width * 0.97
        if self.rect.x < max_width and self.moving_right:
            self.x += self.settings.ship_speed
        if self.rect.x > 0 and self.moving_left:
            self.x -= self.settings.ship_speed
        if self.rect.y > self.settings.screen_height * 0.6 and self.moving_up:
            self.y -= self.settings.ship_speed
        if self.rect.y < self.settings.screen_height * 0.95 and self.moving_down:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
