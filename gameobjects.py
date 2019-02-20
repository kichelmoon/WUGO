import pygame
import userevents
import helpers
import random


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def on_collide(self):
        helpers.log("touched an object")
        return -1


class Door(GameObject):
    def __init__(self, x, y, color):
        super(Door, self).__init__(x, y, color)

    def on_collide(self):
        self.kill()
        return pygame.event.Event(userevents.NEXT_LEVEL, None)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()
