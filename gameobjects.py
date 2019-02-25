import pygame
import userevents
import helpers
from player import Direction


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_width, tile_height, color):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((tile_width, tile_height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def on_player_collide(self):
        return None


class Bullet(GameObject):
    def __init__(self, start_x, start_y, direction, speed):
        super(Bullet, self).__init__(start_x, start_y, 10, 10, (0, 0, 255))
        self.direction = direction
        self.speed = speed

    def update(self, walls):
        if self.direction is Direction.UP:
            self.rect.move_ip(0, -self.speed)
        elif self.direction is Direction.DOWN:
            self.rect.move_ip(0, self.speed)
        elif self.direction is Direction.LEFT:
            self.rect.move_ip(-self.speed, 0)
        elif self.direction is Direction.RIGHT:
            self.rect.move_ip(self.speed, 0)

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.kill()

    def on_player_collide(self):
        self.kill()


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

    def on_player_collide(self):
        self.kill()
        return pygame.event.Event(userevents.NEXT_LEVEL, {})


class Trap(GameObject):
    def __init__(self, x, y, tile_width, tile_height, color):
        super(Trap, self).__init__(x, y, tile_width, tile_height, color)
        self.on = True

    def on_player_collide(self):
        if self.on:
            self.on = False
            return pygame.event.Event(userevents.SWITCH_COLORS, {})
