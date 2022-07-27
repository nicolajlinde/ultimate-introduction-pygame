import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400
FPS = 60
SCORE_FONT = pygame.font.Font("font/Pixeltype.ttf", 25)
points = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

score_surf = SCORE_FONT.render(f"Score: {points}", False, (64, 64, 64))
score_rect = score_surf.get_rect(topleft=(25, 25))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(800, 300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos):
        #         print("Player collided with mouse.")

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.x <= 0:
        snail_rect.x = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(snail_rect):
        print("Collision")

    pygame.display.update()
    clock.tick(FPS)
