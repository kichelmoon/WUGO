class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.door_x = width - 25
        self.door_y = self.height / 2
