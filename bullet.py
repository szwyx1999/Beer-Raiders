import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the player's gun."""

    def __init__(self, screen, settings, x, y):
        """Create a bullet object at the gun's current position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        # Load the bullet image, get image rect, and set current position
        self.bullet = pygame.image.load(self.settings.bulletImg)
        self.rect = self.bullet.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        # Store the bullet's position as a decimal value
        self.yval = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.yval -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.yval

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.bullet, self.rect)