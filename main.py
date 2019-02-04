import pygame
from pygame.locals import *
from player import Player


SCRREN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((SCRREN_WIDTH, SCREEN_HEIGHT))
player = Player(SCRREN_WIDTH, SCREEN_HEIGHT)

game_objects = pygame.sprite.Group()
game_objects.add(player)

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.blit(background, (0, 0))

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    for entity in game_objects:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
