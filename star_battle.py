import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class StarBattle:
    """Class to manage game's behavior and resources."""

    def __init__(self):
        """Initialize pygame with the attributes of the game and create its window."""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Battle")
        self.bg_color = self.settings.rgb

        # Fullscreen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Run the game using the main while loop."""
        while True:
            self._check_events()
            self._update_screen()
            self.bullets.update()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """Listen for mouse and keyboard events while the game is running."""
        for event in pygame.event.get():
            # Quits the game if the condition is matched.
            if event.type == pygame.QUIT:
                sys.exit()

            self._control_game(event)

    def _update_screen(self):
        """Updates the screen after each pass through the while loop"""
        # Fill the screen with the background color.
        self.screen.fill(self.bg_color)

        # Draw the ship.
        self.ship.blit_me()

        # Draw bullets.
        for bullet in self.bullets:
            bullet.draw_bullet()

        # Updates the ship's position.
        self.ship.update_ship_position()

        # Show the most recent drawn screen.
        pygame.display.flip()

    def _control_game(self, event):
        """Control the ship with keyboard events that change a flag attribute of the ship object."""
        if event.type == pygame.KEYDOWN:
            self._move_ship(event)
            # If "q" key is pressed quits the game.
            if event.key == pygame.K_q:
                sys.exit()
            # Shoot bullets if space is pressed
            if event.key == pygame.K_SPACE:
                self._shoot_bullets()
        elif event.type == pygame.KEYUP:
            self._stop_ship(event)

    def _move_ship(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _stop_ship(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _shoot_bullets(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        print(len(self.bullets))


if __name__ == "__main__":
    # Create an instance of StarBattle and run the game.
    sb = StarBattle()
    sb.run_game()
