import pygame
import helpers
from pygame.locals import *
from gameobjects import *
from map import Map


SCRREN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((SCRREN_WIDTH, SCREEN_HEIGHT))
player = Player(SCRREN_WIDTH, SCREEN_HEIGHT)
game_map = Map(SCRREN_WIDTH, SCREEN_HEIGHT)
door = Door(game_map.door_x, game_map.door_y, (255, 0, 0))

game_objects = pygame.sprite.Group()
game_objects.add(door)

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

    for entity in game_objects:
        if player.is_collided_with(entity):
            entity.on_collide()
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
