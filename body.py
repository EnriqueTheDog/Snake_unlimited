from config import WINDOW_WIDTH, WINDOW_HEIGHT


class Body:

    # body directions:
    # 0: up
    # 1: right
    # 2: down
    # 3: left

    def __init__(self, pos, direction, height, width):
        self.position = pos
        self.direction = direction
        self.height = height
        self.width = width

    def move(self, direction):
        if direction == 0:
            self.position[1] -= self.height
        elif direction == 1:
            self.position[0] += self.width
        elif direction == 2:
            self.position[1] += self.height
        elif direction == 3:
            self.position[0] -= self.width

    def over_screen(self, side):
        if side == 0:
            self.position[1] = WINDOW_HEIGHT - self.height
        elif side == 1:
            self.position[0] = 0
        elif side == 2:
            self.position[1] = 0
        elif side == 3:
            self.position[0] = WINDOW_WIDTH - self.width