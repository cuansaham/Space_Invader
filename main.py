import pygame
import random
from player import Player
from settings import WHITE,RED,GREEN,WIDTH,HEIGHT

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)