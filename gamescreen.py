import pygame
from settings import WIDTH, HEIGHT, BLACK, WHITE, RED, GREEN

class GameScreen:

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
    
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("SPACE INVADERS", 50, WHITE, WIDTH // 2, HEIGHT // 4)
        self.draw_text("Press Enter to start", 30, WHITE, WIDTH // 2, HEIGHT // 2)
        self.draw_text("Or Esc to exit", 30, WHITE, WIDTH // 2, HEIGHT * 3 // 4)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 50, RED, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds

    def show_victory_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("VICTORY!", 50, GREEN, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds
