import pygame
from settings import *


class Bird(pygame.sprite.Sprite):

    def __init__(self, path, speed, x, y):
        """Bird's sprite init"""
        pygame.init()
        super(Bird, self).__init__()
        self.path = path
        self.step = 1
        self.surf = pygame.image.load(self.path+'/frame-' + str(self.step) + '.png')
        self.rect = self.surf.get_rect()
        self.speed = speed
        self.rect = self.surf.get_rect(left=x, top=y)

    def update(self):
        """Update bird's animation and position on the screen """
        if self.step == 4:
            self.step = 1
        else:
            self.step += 1
        self.surf = pygame.image.load(self.path+'/frame-' + str(self.step) + '.png')
        if self.rect.left < abs(WIDTH - 20) or self.rect.top < abs(HEIGHT - 20):
            self.rect.left += self.speed
        else:
            self.kill()
