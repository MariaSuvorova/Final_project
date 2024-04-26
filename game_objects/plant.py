import pygame
from settings import *

class Plant(pygame.sprite.Sprite):

    def __init__(self, path, x, y):
        """Plant's sprite init"""
        super(Plant, self).__init__()
        self.path = path
        self.step = 1
        self.surf = pygame.image.load(self.path+'/frame-' + str(self.step) + '.png')
        self.rect = self.surf.get_rect()
        self.rect = self.surf.get_rect(left=x, top=y)

    def update(self):
        """Update plant's animation"""
        if self.step == 7:
            self.step = 1
        else:
            self.step += 1
        self.surf = pygame.image.load(self.path+'/frame-' + str(self.step) + '.png')
