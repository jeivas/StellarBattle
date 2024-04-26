import sys
import pygame

from button import Button
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        self.running = False

        # Create a sprite group and add the button to make it easier to remove it later
        self.button_container = pygame.sprite.Group()
        self.button_container.add(Button(self))

        # Setup game elements.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Points system
        self.points = 0

    def run_game(self):
        """Run the game using the main while loop."""
        while True:
            self._check_events()
            self._update_screen()
            self.bullets.update()
            self.aliens.update()
            self._kill_alien()
            self._control_difficult()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """Listen for mouse and keyboard events while the game is running."""
        for event in pygame.event.get():
            # Quits the game if the condition is matched.
            if event.type == pygame.QUIT:
                sys.exit()

            self._control_game(event)
            self._check_button_click(event)

    def _update_screen(self):
        """Updates the screen after each pass through the while loop"""
        # Fill the screen with the background color.
        self.screen.fill(self.bg_color)

        if len(self.button_container) > 0:
            self.button_container.update()

        # Draw the ship.
        self.ship.blit_me()

        if self.running:
            # Create alien if the condition is matched.
            if len(self.aliens) < self.settings.aliens_max:
                new_alien = Alien(self)
                self.aliens.add(new_alien)

            # Show each alien in its current position.
            for alien in self.aliens:
                alien.blit_me()

            # Draw bullets.
            for bullet in self.bullets:
                bullet.draw_bullet()

            self.ship.update_ship_position()

        self._show_score()

        # Show the most recent drawn screen.
        pygame.display.flip()

    def _control_game(self, event):
        """Control the ship with keyboard events that change a flag attribute of the ship object."""
        if event.type == pygame.KEYDOWN:
            self._move_ship(event)
            # If "q" key is pressed quits the game.
            if event.key == pygame.K_q:
                sys.exit()
            # Shoot bullets if space is pressed.
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
        """Create a new bullet object and add to sprites group."""
        if len(self.bullets) < self.settings.bullet_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _kill_alien(self):
        """Delete alien object."""
        for alien in self.aliens:
            # Kill alien object if it passes the screen limit and remove a point.
            if alien.rect.top > self.settings.alien_max_deep:
                alien.kill()
                self._remove_point()
            for bullet in self.bullets:
                # Kill alien object if it collides with the bullet and score a poit.
                if alien.rect.collidepoint(bullet.rect.x, bullet.rect.y):
                    alien.kill()
                    bullet.kill()
                    self._score_point()

    def _score_point(self):
        self.points += 1

    def _remove_point(self):
        self.points -= 1

    def _control_difficult(self):
        """Control game difficult based in the number of points"""
        if self.points > 5:
            self.settings.aliens_max = 4
        elif self.points > 10:
            self.settings.aliens_max = 5
        elif self.points > 20:
            self.settings.aliens_max = 6

    def draw_text(self, x, y, string, col, size):
        font = pygame.font.SysFont("Impact", size)
        text = font.render(string, True, col)
        textbox = text.get_rect()
        textbox.center = (x, y)
        self.screen.blit(text, textbox)

    def _show_score(self):
        """Style the scoreboard and display it on screen"""
        x = self.settings.points_position[0]
        y = self.settings.points_position[1]

        # TEXT OUTLINE

        # top left
        self.draw_text(x - 2, y - 2, str(self.points), self.settings.font_border_color, 40)
        # top right
        self.draw_text(x + 2, y - 2, str(self.points), self.settings.font_border_color, 40)
        # btm left
        self.draw_text(x - 2, y + 2, str(self.points), self.settings.font_border_color, 40)
        # btm right
        self.draw_text(x + 2, y + 2, str(self.points), self.settings.font_border_color, 40)

        # TEXT FILL

        self.draw_text(x, y, str(self.points), pygame.Color(255, 255, 255), 40)

    def _check_button_click(self, event):
        for button in self.button_container:
            if event.type == pygame.MOUSEBUTTONDOWN and button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.running = True
                button.delete_button()


if __name__ == "__main__":
    # Create an instance of StarBattle and run the game.
    sb = StarBattle()
    sb.run_game()
