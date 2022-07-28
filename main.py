import random
import pygame
from sys import exit
from player import Player
from obstacle import Obstacle


def display_score():
    current_time = f"{int(pygame.time.get_ticks() / 1000) - start_time}"
    score_surf = SCORE_FONT.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(topleft=(25, 25))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_surf, score_rect)


def collisions():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


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

# Music
background_music = pygame.mixer.Sound("audio/music.wav")
background_music.set_volume(0.2)
background_music.play(loops=-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Environment
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

# Game Over Text
game_over_surf = GAME_OVER_FONT.render("GAME OVER", False, (64, 64, 64))
game_over_rect = game_over_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Restart Text
restart_surf = RESTART_FONT.render('PRESS "R" OR "SPACE BAR" TO RESTART', False, (64, 64, 64))
restart_rect = restart_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Add speed


while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_item = ["fly", "snail", "snail", "snail"]
                obstacle_group.add(Obstacle(random.choice(obstacle_item)))
        else:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_r or event.key == pygame.K_SPACE):
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        # Environment
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Time
        display_score()

        # Collision
        game_active = collisions()
    else:
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(restart_surf, restart_rect)
        player_gravity = 0

    pygame.display.update()
    clock.tick(FPS)
