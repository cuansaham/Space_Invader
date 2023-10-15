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
all_sprites.add(player)

alien_width = 50
alien_height =30
alien_gap = 10

aliens = []

for row in range(3):
    for column in range(8):
        x = column * (alien_width + alien_gap)
        y = row * (alien_height + alien_gap)
        alien = Alien(x,y)
        aliens.append(alien)


for alien in aliens:
    all_sprites.add(alien)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    move_down = False
    for alien in aliens:
        if alien.rect.x > WIDTH - 40 or alien.rect.x < 0:
            Alien.direction *= -1
    #         move_down = True
    #         break
    # if move_down:
    #     for alien in aliens:
    #         alien.rect.y +=40
    
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, aliens, False)
    if hits: # If player gets hit by an alien
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)