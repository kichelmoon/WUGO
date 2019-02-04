class Map:
    def __init__(self, width, height):
        self.width = width / 10
        self.height = height / 10
        self.door_x = (self.width - 2) * 10
        self.door_y = self.height * 10
