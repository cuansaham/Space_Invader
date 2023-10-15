import pygame
from settings import RED,WIDTH,HEIGHT
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40,25])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH -40)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1,3)
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, WIDTH -40)
