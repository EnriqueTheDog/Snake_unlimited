import random
from config import WINDOW_HEIGHT, WINDOW_WIDTH
from util import random_color


class Fruit:

    def __init__(self, size):
        self.size = size
        self.position = [random.randint(0, WINDOW_WIDTH - size),
                         random.randint(0, WINDOW_HEIGHT - size)]
        self.color = random_color()
