import pygame
from pygame.locals import *
from gameobjects import *
from map import Map


SCRREN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((SCRREN_WIDTH, SCREEN_HEIGHT))
player = Player(SCRREN_WIDTH, SCREEN_HEIGHT)
game_map = Map(SCRREN_WIDTH, SCREEN_HEIGHT)

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

    screen.blit(player.surf, player.rect)

    for entity in game_map.game_objects:
        if player.is_collided_with(entity):
            event = entity.on_collide()
            if event != -1:
                pygame.event.post(event)
        screen.blit(entity.surf, entity.rect)

    for event in pygame.event.get():
        if event.type == userevents.NEXT_LEVEL:
            game_map = Map(SCRREN_WIDTH, SCREEN_HEIGHT)

    pygame.display.flip()
