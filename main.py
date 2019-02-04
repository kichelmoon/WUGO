import pygame
from pygame.locals import *
from player import Player
pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
player = Player()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.blit(player.surf, player.rect)
    pygame.display.flip()