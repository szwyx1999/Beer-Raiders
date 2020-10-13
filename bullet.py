import pygame
from pygame.sprite import Sprite

class Bullet (Sprite):

    def __init__(self, settings, screen, player):
        # create a bullet at the location of the player
        super(Bullet, self).__init__()
        self.screen = screen

        # set the location of the bullet
        