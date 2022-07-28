import pygame
from sys import exit


def display_score():
    current_time = f"{int(pygame.time.get_ticks() / 1000) - start_time}"
    score_surf = SCORE_FONT.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(topleft=(25, 25))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_surf, score_rect)


pygame.init()

WIDTH = 800
HEIGHT = 400
FPS = 60
SCORE_FONT = pygame.font.Font("font/Pixeltype.ttf", 25)
GAME_OVER_FONT = pygame.font.Font("font/Pixeltype.ttf", 75)
RESTART_FONT = pygame.font.Font("font/Pixeltype.ttf", 25)
score = 0
game_active = True
start_time = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# Environment
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

# Game Over Text
game_over_surf = GAME_OVER_FONT.render("GAME OVER", False, (64, 64, 64))
game_over_rect = game_over_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Restart Text
restart_surf = RESTART_FONT.render('PRESS "R" OR "SPACE BAR" TO RESTART', False, (64, 64, 64))
restart_rect = restart_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))

# Enemies
snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(800, 300))

# Player
player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
                player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r or event.key == pygame.K_SPACE:
                    snail_rect.x = 800
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        # Environment
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        # Enemies
        snail_rect.x -= 4
        if snail_rect.x <= 0:
            snail_rect.x = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf, player_rect)

        # Time
        display_score()

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(restart_surf, restart_rect)

    pygame.display.update()
    clock.tick(FPS)
