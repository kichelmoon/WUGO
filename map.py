import random
import pygame
from gameobjects import Door


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.door = Door(width - 25, self.height - random.randint(0, self.height - 25), (255, 0, 0))
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.door)
