import pygame
from bullet import Bullet

class Player:
    """A class to manage the player."""

    def __init__(self, br_game):
        """Initialize the player and set its starting position."""
        self.is_animating = False
        # animation to walk right
        self.walkRight = [pygame.image.load('BRsprites/RshootUp(1).png'), pygame.image.load('BRsprites/RshootUp(2).png'),
                          pygame.image.load('BRsprites/RshootUp(3).png'), pygame.image.load('BRsprites/RshootUp(4).png')]

        # animation to walk left
        self.walkLeft = [pygame.image.load('BRsprites/LshootUp(1).png'), pygame.image.load('BRsprites/LshootUp(2).png'),
                         pygame.image.load('BRsprites/LshootUp(3).png'), pygame.image.load('BRsprites/LshootUp(4).png')]

        self.screen = br_game.screen
        self.settings = br_game.settings
        self.screen_rect = br_game.screen.get_rect()

        # Load the player image and get its rect
        self.current_sprite = 0
        self.image = self.walkLeft[self.current_sprite]
        self.rect = self.image.get_rect()

        self.bullets = pygame.sprite.Group()
        self.prevMv = 'moveleft'

        self.x = float(self.rect.x)
        self.moving_left = False
        self.moving_right = False

        # Start each new player at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def shoot(self):
        """Create a new bullet and add it to the bullets group."""
        if self.moving_right:
            if len(self.bullets) < self.settings.bullets_allowed:
                bullet = Bullet(self.screen, self.settings,
                                self.rect.right, self.rect.top)
                self.bullets.add(bullet)
        elif self.moving_left:
            if len(self.bullets) < self.settings.bullets_allowed:
                bullet = Bullet(self.screen, self.settings,
                                self.rect.left, self.rect.top)
                self.bullets.add(bullet)
        else:
            if self.prevMv == 'moveright':
                if len(self.bullets) < self.settings.bullets_allowed:
                    bullet = Bullet(self.screen, self.settings,
                                    self.rect.right, self.rect.top)
                    self.bullets.add(bullet)
            elif self.prevMv == 'moveleft':
                if len(self.bullets) < self.settings.bullets_allowed:
                    bullet = Bullet(self.screen, self.settings,
                                    self.rect.left, self.rect.top)
                    self.bullets.add(bullet)

    def animate(self, runAnimation):
        self.is_animating = runAnimation

    def update(self):
        """Update the player's position based on movement flags."""
        if self.is_animating:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.current_sprite += self.settings.animate_speed
                self.x += self.settings.player_speed
                if self.current_sprite >= len(self.walkRight):
                    self.current_sprite = 0
                self.image = self.walkRight[int(self.current_sprite)]
            if self.moving_left and self.rect.left > 0:
                self.current_sprite += self.settings.animate_speed
                self.x -= self.settings.player_speed
                if self.current_sprite >= len(self.walkLeft):
                    self.current_sprite = 0
                self.image = self.walkLeft[int(self.current_sprite)]
        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_player(self):
        """Center the player on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)