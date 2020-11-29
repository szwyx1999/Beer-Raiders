from os import path
from settings import Settings
from player import Player
import pygame
import random
import math
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
        # clock
        #self.clock = pygame.time.Clock()
        # Background
        self.background = pygame.image.load(self.settings.background)
        # Title and Icon
        pygame.display.set_caption("Beer Raiders")
        pygame.display.set_icon(pygame.image.load('alcohol.png'))

        self.player = Player(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.player.update()
            self._update_bullets()
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

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
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
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.player.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.player.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.player.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.player.blitme()
        for bullet in self.player.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        #self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game
    br = BeerRaiders()
    br.run_game()

# Enemy
# enemyImg = []
# enemyX = []
# enemyY = []
# enemyX_change = []
# enemyY_change = []
# num_of_enemies = 6
#
# for i in range(num_of_enemies):
#     enemyImg.append(pygame.image.load("images/alienship.png"))
#     enemyX.append(random.randint(0, 886))
#     enemyY.append(random.randint(50, 150))
#     enemyX_change.append(12)
#     enemyY_change.append(40)
#
# score
# score_value = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
# textX = 10
# textY = 10
#
# game over font
# over_font = pygame.font.Font('freesansbold.ttf', 85)
#
# def show_score(x, y):
#     score = font.render("Score: " + str(score_value), True, (0, 0, 0))
#     screen.blit(score, (x, y))
#
# def game_over_text():
#     over_text = over_font.render("GAME OVER", True, (0, 0, 0))
#     screen.blit(over_text, (230, 320))
#
# def enemy(x, y, i):
#     screen.blit(enemyImg[i], (x, y))
#
# def isCollision(enemyX, enemyY, bulletX, bulletY):
#     distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
#     if distance < 25:
#         return True
#     else:
#         return False
#
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
    #
    # enemy movement
    # for i in range(num_of_enemies):
    #
        # game over
        # if enemyY[i] > 610:
        #     for j in range(num_of_enemies):
        #         enemyY[j] = 2000
        #     game_over_text()
        #     break
        # enemyX[i] += enemyX_change[i]
        # if enemyX[i] <= 0:
        #     enemyX_change[i] = 12
        #     enemyY[i] += enemyY_change[i]
        # elif enemyX[i] >= 886:
        #     enemyX_change[i] = -12
        #     enemyY[i] += enemyY_change[i]
        #
        # collision
        # collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        # if collision:
        #     bulletY = 620
        #     bullet_state = "ready"
        #     score_value += 1
        #     enemyX[i] = random.randint(0, 886)
        #     enemyY[i] = random.randint(50, 150)
        #
        # enemy(enemyX[i], enemyY[i], i)
