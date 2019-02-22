import helpers
from level import Level
from gameobjects import Brick, Wall


class Maploader:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def load_map(self, name):
        with open(name + '.lv') as levelfile:
            content = levelfile.readlines()
            level_lines = [x.strip() for x in content]

            tile_width = self.width / len(level_lines[0])
            tile_height = self.height / len(level_lines)

            helpers.log(tile_width)
            helpers.log(tile_height)

            level = Level(self.width, self.height)
            x = 0
            y = 0
            for level_line in level_lines:
                for tile in level_line:
                    if tile == "#":
                        level.add_game_object(Brick(x, y, tile_width, tile_height))
                    elif tile == "B":
                        level.add_game_object(Wall(x, y, tile_width, tile_height, True))
                    elif tile == "W":
                        level.add_game_object(Wall(x, y, tile_width, tile_height, False))

                    x += tile_width
                x = 0
                y += tile_height

            return level
