from typing import Tuple
import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, path):
        """Player's sprite init"""
        super(Player, self).__init__()
        self.step = 1
        self.path = path
        player_image = str(self.path+'/frame-' + str(self.step) + '.png')
        self.surf = pygame.image.load(player_image)
        self.rect = self.surf.get_rect()

    def update(self, pos: Tuple):
        """Update player's animation and position (mouse depend)"""
        if self.step == 6:
            self.step = 1
        else:
            self.step += 1
        self.rect.center = pos
        player_image = str(self.path+'/frame-' + str(self.step) + '.png')
        self.surf = pygame.image.load(player_image)
