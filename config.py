from util import random_color
from pygame import time, font, display

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 20, 20)
RANDOM = random_color()

# Game Setup
FPS = 9
fpsClock = time.Clock()
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 550

# Initialise window
WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('Snake Ultimate')

# Snake and fruit config
SNAKE_POSITION = [300, 250]
SNAKE_SIZE = 25
FRUIT_SIZE = 10

# fonts
font.init()

BASIC_FONT = font.SysFont('DejaVu Sans Mono', 22)
BIG_FONT = font.SysFont('DejaVu Sans Mono', 33)