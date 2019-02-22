import pygame
import helpers
from pygame.locals import *


class Stats:
    def __init__(self, start_speed, start_hp):
        self.speed = start_speed
        self.hp = start_hp


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, start_stats):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()
        self.max_width = screen.width
        self.max_height = screen.height
        self.stats = start_stats
        self.x_speed = 0
        self.y_speed = 0

    def update(self, pressed_keys, walls):
        if pressed_keys[K_UP]:
            self.y_speed = -self.stats.speed
        elif pressed_keys[K_DOWN]:
            self.y_speed = self.stats.speed
        else:
            self.y_speed = 0

        if pressed_keys[K_LEFT]:
            self.x_speed = -self.stats.speed
        elif pressed_keys[K_RIGHT]:
            self.x_speed = self.stats.speed
        else:
            self.x_speed = 0

        new_rect = self.rect.move(self.x_speed, self.y_speed)

        for wall in walls:
            if new_rect.colliderect(wall.rect):
                return

        self.rect = new_rect

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
