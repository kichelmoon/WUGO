from gameobjects import *


class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.background = pygame.Surface((width, height))
        self.background.fill((0, 0, 0))

        self.moving_objects = pygame.sprite.Group()
        self.black_world = pygame.sprite.Group()
        self.white_world = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.game_objects = pygame.sprite.Group()

    def add_game_object(self, game_object):
        if isinstance(game_object, Wall):
            if game_object.black_wall:
                self.black_world.add(game_object)
            else:
                self.white_world.add(game_object)
        if isinstance(game_object, Brick):
            self.bricks.add(game_object)
        else:
            self.game_objects.add(game_object)

    def switch_background(self, black_mode):
        if black_mode:
            self.background.fill((255, 255, 255))
        else:
            self.background.fill((0, 0, 0))

    def get_walls_for_mode(self, black_mode):
        return_group = pygame.sprite.Group()
        return_group.add(self.bricks)
        if not black_mode:
            return_group.add(self.black_world)
        else:
            return_group.add(self.white_world)

        return return_group
