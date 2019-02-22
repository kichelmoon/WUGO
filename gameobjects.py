import pygame
import userevents
import helpers


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_width, tile_height, color):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((tile_width, tile_height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def on_collide(self):
        helpers.log(["touched an object"])
        return None


class Wall(GameObject):
    def __init__(self, x, y, tile_width, tile_height, dark_wall):
        if dark_wall:
            color = (0, 0, 0)
        else:
            color = (255, 255, 255)
        self.black_wall = dark_wall

        super(Wall, self).__init__(x, y, tile_width, tile_height, color)


class Brick(GameObject):
    def __init__(self, x, y, tile_width, tile_height):
        color = (122, 122, 122)

        super(Brick, self).__init__(x, y, tile_width, tile_height, color)


class Door(GameObject):
    def __init__(self, x, y, tile_width, tile_height, color):
        super(Door, self).__init__(x, y, tile_width, tile_height, color)

    def on_collide(self):
        self.kill()
        return pygame.event.Event(userevents.NEXT_LEVEL, {})


class Trap(GameObject):
    def __init__(self, x, y, tile_width, tile_height, color):
        super(Trap, self).__init__(x, y, tile_width, tile_height, color)
        self.on = True

    def on_collide(self):
        if self.on:
            self.on = False
            return pygame.event.Event(userevents.SWITCH_COLORS, {})
