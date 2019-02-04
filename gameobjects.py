import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()
        self.max_width = screen_width
        self.max_height = screen_height
        self.speed = 2

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.max_width:
            self.rect.right = self.max_width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.max_height:
            self.rect.bottom = self.max_height

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def on_collide(self):
        print("done")
        self.kill()


class Door(GameObject):
    def __init__(self, x, y, color):
        super(Door, self).__init__(x, y, color)

    def on_collide(self):
        print("next level shit")