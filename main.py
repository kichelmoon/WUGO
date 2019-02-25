from gameobjects import *
from level import Level
from player import *
from maploader import Maploader


class GameScreen:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height


def draw_group(group, screen):
    for entity in group:
        screen.blit(entity.surf, entity.rect)


pygame.init()
game_screen = GameScreen(800, 600)
screen = pygame.display.set_mode((game_screen.width, game_screen.height))

my_map_loader = Maploader(800, 600)
start_stats = Stats(5, 100)
player = Player(game_screen, start_stats)
level = my_map_loader.load_map('level1')

clock = pygame.time.Clock()
running = True
is_black_mode = True
pygame.time.set_timer(userevents.SWITCH_COLORS, 250)

while running:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
        elif e.type == QUIT:
            running = False

    screen.blit(level.background, (0, 0))

    walls = level.get_walls_for_mode(is_black_mode)
    draw_group(walls, screen)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, walls)

    screen.blit(player.surf, player.rect)

    for entity in level.moving_objects:
        entity.update(walls)
        screen.blit(entity.surf, entity.rect)

    for entity in level.game_objects:
        if player.is_collided_with(entity):
            e = entity.on_player_collide()
            if e is not None:
                pygame.event.post(e)

        screen.blit(entity.surf, entity.rect)

    for e in pygame.event.get():
        if e.type == userevents.NEXT_LEVEL:
            level = Level(game_screen.width, game_screen.height)
        if e.type == userevents.SWITCH_COLORS:
            level.switch_background(is_black_mode)
            is_black_mode = not is_black_mode
        if e.type == userevents.FIRE_BULLET:
            level.moving_objects.add(Bullet(e.x, e.y, e.dir, e.speed))
            helpers.log([e.x, e.y])
    pygame.display.flip()
