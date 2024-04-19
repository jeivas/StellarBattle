import sys
import pygame
from settings import Settings
from ship import Ship


class StarBattle:
    """"Class to manage game's behavior and resources"""

    def __init__(self):
        """Initialize pygame and create game's window"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Star Battle")
        self.bg_color = self.settings.rgb
        self.ship = Ship(self)

    def run_game(self):
        """"Run the game using the main while loop"""
        while True:
            # Listen for pygame events
            for event in pygame.event.get():
                # Condition to quit the game
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraws the screen on each loop
            self.screen.fill(self.bg_color)

            # Draws the ship
            self.ship.blit_me()

            # Shows the most recent drawn screen
            pygame.display.flip()
            self.clock.tick(self.settings.fps)


if __name__ == "__main__":
    # Creates an instance and runs the game
    sb = StarBattle()
    sb.run_game()
