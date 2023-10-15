import pygame
import random
from player import Player
from settings import WHITE,RED,GREEN,BLACK,WIDTH,HEIGHT
from alien import Alien
from bullet import Bullet
from gamescreen import GameScreen

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

aliens = pygame.sprite.Group()

for row in range(4):
    for column in range(10):
        x = column * (alien_width + alien_gap)
        y = row * (alien_height + alien_gap)
        alien = Alien(x,y)
        aliens.add(alien)


for alien in aliens:
    all_sprites.add(alien)

player_bullets = pygame.sprite.Group()
alien_bullets = pygame.sprite.Group()
game_screen = GameScreen(screen)
game_screen.show_start_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.x + player.rect.width //2, player.rect.y,1)
                player_bullets.add(bullet)
                all_sprites.add(bullet)
    move_down = False
    for alien in aliens:
        if alien.rect.x > WIDTH - 40 or alien.rect.x < 0:
            Alien.direction *= -1
            move_down = True
            break
    if move_down:
        for alien in aliens:
            alien.rect.y +=40
    
    if random.random() < 0.02:
        if aliens.sprites():
            shooting_alien = random.choice(aliens.sprites())
            bullet = Bullet(shooting_alien.rect.x + shooting_alien.rect.width // 2,shooting_alien.rect.y + shooting_alien.rect.height, -1)
            alien_bullets.add(bullet)
            all_sprites.add(bullet)
    
    all_sprites.update()

    player_hits = pygame.sprite.spritecollide(player, alien_bullets, False)
    for hit in player_hits:
        if hit.direction == -1: #Alien bullet
            running = False
    
    alien_hits = pygame.sprite.groupcollide(aliens, player_bullets, False, True)
    for alien, bullet_list in alien_hits.items():
        for b in bullet_list:
            if b.direction == 1 :
                alien.kill()

    for hit in alien_hits:
        # Later 
        pass


    hits = pygame.sprite.spritecollide(player, aliens, False)
    if hits: # If player gets hit by an alien
        running = False 
    
    if len(aliens) == 0:
        running = False
    
    if not running:
        if len(aliens) == 0:
            game_screen.show_victory_screen()
        else :
            game_screen.show_game_over_screen()
        game_screen.show_start_screen()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)