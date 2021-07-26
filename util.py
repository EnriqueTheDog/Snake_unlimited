import random


def random_color():
    result = []
    for x in range(3):
        result.append(random.randint(120, 255))
    return result


def turn(direction, clock=True):
    if clock:
        direction += 1
        if direction > 3:
            direction = 0
    else:
        direction -= 1
        if direction < 0:
            direction = 3
    return direction


def intersect(fruit, snake):
    fruit_x = set(range(fruit.position[0], fruit.position[0] + fruit.size))
    fruit_y = set(range(fruit.position[1], fruit.position[1] + fruit.size))
    snake_x = set(range(snake.head.position[0], snake.head.position[0] + snake.head.width))
    snake_y = set(range(snake.head.position[1], snake.head.position[1] + snake.head.height))

    if fruit_x.intersection(snake_x) and fruit_y.intersection(snake_y):
        return True
    else:
        return False