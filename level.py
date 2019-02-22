import random
import pygame
from gameobjects import Wall, Door, Trap


class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.background = pygame.Surface((width, height))
        self.background.fill((0, 0, 0))

        self.door = Door(width - 25, self.height - random.randint(0, self.height - 25), (255, 0, 0))

        self.moving_objects = pygame.sprite.Group()

        self.black_walls = pygame.sprite.Group()
        self.black_walls.add(Wall(0, 25, True))
        self.black_walls.add(Wall(0, 50, True))
        self.black_walls.add(Wall(0, 75, True))

        self.white_walls = pygame.sprite.Group()
        self.white_walls.add(Wall(25, 50, False))

        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(Trap(50, 50, (0, 0, 255)))
        self.game_objects.add(self.door)
        self.game_objects.add(self.moving_objects)

    def switch_background(self, black_mode):
        if black_mode:
            self.background.fill((255, 255, 255))
            self.backgroundBlack = False
        else:
            self.background.fill((0, 0, 0))
            self.backgroundBlack = True
