from gameobjects import *


class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.background = pygame.Surface((width, height))
        self.background.fill((0, 0, 0))

        self.moving_objects = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.game_objects = pygame.sprite.Group()

    def add_game_object(self, game_object):
        self.game_objects.add(game_object)

    def switch_background(self, black_mode):
        if black_mode:
            self.background.fill((255, 255, 255))
        else:
            self.background.fill((0, 0, 0))

