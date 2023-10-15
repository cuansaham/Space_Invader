import pygame
from settings import RED,WIDTH,HEIGHT
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([30,20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    direction = 1

    def update(self):
        self.rect.x += self.speed * Alien.direction
