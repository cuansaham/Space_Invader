import pygame
import random
from player import Player
from settings import WHITE,RED,GREEN,WIDTH,HEIGHT
from alien import Alien

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

player = Player()
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
all_sprites.add(player)

for i in range(5):
    alien = Alien()
    all_sprites.add(alien)
    aliens.add(alien)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, aliens, False)
    if hits: # If player gets hit by an alien
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)