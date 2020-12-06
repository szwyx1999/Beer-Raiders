from os import path
from settings import Settings
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from player import Player
from alien import Alien
from time import sleep
import pygame
import sys

class BeerRaiders:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # create the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # Background
        self.background = pygame.image.load(self.settings.background)
        # Title and Icon
        pygame.display.set_caption("Beer Raiders")
        pygame.display.set_icon(pygame.image.load('alcohol.png'))
        # Create an instance to store game statistics, and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        # Create player object to implement the creation and update of bullets
        self.player = Player(self)
        # Create group of alien sprites and create fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Make the play button
        self.play_button = Button(self, "Play Game")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.player.animate(True)
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.player.animate(False)
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_beers()
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.player.bullets.empty()
            # Create a new fleet and center the player
            self._create_fleet()
            self.player.center_player()
            # Hide mouse cursor
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to key presses."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
            self.player.moving_right = False
            self.player.prevMv = 'moveright'
            self.player.shoot()
        elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
            self.player.moving_left = False
            self.player.prevMv = 'moveleft'
            self.player.shoot()
        elif keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.player.moving_left = False
            self.player.moving_right = False
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.player.shoot()


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
            self.player.prevMv = 'moveright'
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
            self.player.prevMv = 'moveleft'


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.player.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.player.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.player.bullets.remove(bullet)
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.player.bullets,
                                                self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.player.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-player collisions
        if pygame.sprite.spritecollideany(self.player, self.aliens):
            self._player_hit()
        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the player got hit
                self._player_hit()
                break


    def _player_hit(self):
        """Respond to the player being hit by an alien."""
        if self.stats.beers_left > 0:
            # Decrement beers_left, and update scoreboard
            self.stats.beers_left -= 1
            self.sb.prep_beers()
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.player.bullets.empty()
            # Create a new fleet and center the player
            self._create_fleet()
            self.player.center_player()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fit on the screen
        player_height = self.player.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - player_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.player.blitme()
        for bullet in self.player.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Draw the score information
        self.sb.show_score()
        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    br = BeerRaiders()
    br.run_game()


######################################
######################################
# """
# Explosion
# """
# Define Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
#
# Get the path of images
# img_dir = path.join(path.dirname(__file__), 'images')
#
# class Explosion(pygame.sprite.Sprite):
#     def __init__(self, center, size):
#         pygame.sprite.Sprite.__init__(self)
#         self.size = size
#         self.image = explosion_animation[self.size][0]
#         self.rect = self.image.get_rect()
#         self.rect.center = center
#         self.frame = 0
#         self.last_update = pygame.time.get_ticks()
#         self.frame_rate = 75
#
#     def Exp_update(self):
#         now = pygame.time.get_ticks()
#         if now - self.last_update > self.frame_rate:
#             self.last_update = now
#             self.frame += 1
#             if self.frame == len(explosion_animation[self.size]):
#                 self.kill()
#             else:
#                 center = self.rect.center
#                 self.image = explosion_animation[self.size][self.frame]
#                 self.rect = self.image.get_rect()
#                 self.rect.center = center
#
# Load Explosion images
# explosion_animation = []
# for i in range(1, 9):
#     filename = 'explosion_{}.png'.format(i)
#     img = pygame.image.load(path.join(img_dir, filename)).convert()
#     img.set_colorkey(BLACK)
#     change the size of the explosion
#     img_size = pygame.transform.scale(img, (60, 60))
#     explosion_animation.append(img_size)
#
######################################
######################################
