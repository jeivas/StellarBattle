import sys
import pygame
from settings import Settings
from ship import Ship


class StarBattle:
    """"Class to manage game's behavior and resources."""

    def __init__(self):
        """Initialize pygame with the attributes of the game and create its window."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Star Battle")
        self.bg_color = self.settings.rgb
        self.ship = Ship(self)

    def run_game(self):
        """"Run the game using the main while loop."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    @staticmethod
    def _check_events():
        """Listen for mouse and keyboard events while the game is running."""
        for event in pygame.event.get():
            # Quits the game if the condition is matched
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Fill the screen with the background color.
        self.screen.fill(self.bg_color)
        # Draws the ship.
        self.ship.blit_me()
        # Show the most recent drawn screen.
        pygame.display.flip()


if __name__ == "__main__":
    # Create an instance and run the game.
    sb = StarBattle()
    sb.run_game()
