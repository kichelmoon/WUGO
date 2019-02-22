import pygame
import userevents
import helpers


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def on_collide(self):
        helpers.log(["touched an object"])
        return None


class Wall(GameObject):
    def __init__(self, x, y, dark_wall):
        if dark_wall:
            color = (0, 0, 0)
        else:
            color = (255, 255, 255)

        super(Wall, self).__init__(x, y, color)


class Door(GameObject):
    def __init__(self, x, y, color):
        super(Door, self).__init__(x, y, color)

    def on_collide(self):
        self.kill()
        return pygame.event.Event(userevents.NEXT_LEVEL, {})


class Trap(GameObject):
    def __init__(self, x, y, color):
        super(Trap, self).__init__(x, y, color)
        self.on = True

    def on_collide(self):
        if self.on:
            self.on = False
            return pygame.event.Event(userevents.SWITCH_COLORS, {})
