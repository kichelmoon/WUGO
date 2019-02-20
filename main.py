from gameobjects import *
from map import Map
from player import *


class GameScreen:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height


pygame.init()
game_screen = GameScreen(800, 600)
screen = pygame.display.set_mode((game_screen.width, game_screen.height))

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

start_stats = Stats(5, 100)
player = Player(game_screen, start_stats)
game_map = Map(game_screen.width, game_screen.height)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.blit(background, (0, 0))

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.blit(player.surf, player.rect)

    for entity in game_map.game_objects:
        if player.is_collided_with(entity):
            event = entity.on_collide()
            if event != -1:
                pygame.event.post(event)
        screen.blit(entity.surf, entity.rect)

    for event in pygame.event.get():
        if event.type == userevents.NEXT_LEVEL:
            game_map = Map(game_screen.width, game_screen.height)

    pygame.display.flip()
