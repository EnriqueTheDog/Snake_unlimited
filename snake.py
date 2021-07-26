import body
from util import turn, random_color
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS


class Snake:

    def __init__(self, pos, direction, size):
        self.head = body.Body(pos, direction, size, size)
        self.body = [self.head]
        self.size = size
        self.moves = [direction]
        self.color = random_color()
        self.speed = float(FPS)

    def grow(self):
        if self.moves[-1] == 0:
            x = self.body[-1].position[0]
            y = self.body[-1].position[1] + self.size
        elif self.moves[-1] == 1:
            x = self.body[-1].position[0] - self.size
            y = self.body[-1].position[1]
        elif self.moves[-1] == 2:
            x = self.body[-1].position[0]
            y = self.body[-1].position[1] - self.size
        else:
            x = self.body[-1].position[0] + self.size
            y = self.body[-1].position[1]
        new_body = body.Body([x, y], self.body[-1].direction, self.size, self.size)
        self.body.append(new_body)
        self.moves.append(self.moves[-1])

    def order(self, clock=None):
        if clock is None:
            self.moves.insert(0, self.moves[0])
        else:
            self.moves.insert(0, turn(self.moves[0], clock))
        self.moves.pop(-1)

    def creep(self):
        for x in range(len(self.body)):
            self.body[x].move(self.moves[x])

    def overscreen(self):
        for chunk in self.body:
            if chunk.position[1] < 0:
                chunk.over_screen(0)
            if chunk.position[0] + chunk.width > WINDOW_WIDTH:
                chunk.over_screen(1)
            if chunk.position[1] + chunk.width > WINDOW_HEIGHT:
                chunk.over_screen(2)
            if chunk.position[0] < 0:
                chunk.over_screen(3)

    def die(self):
        # check if there are duplicated positions
        position_list = []
        position_set = set()
        for chunk in self.body:
            position_list.append(str(chunk.position))
            position_set.add(str(chunk.position))
        if len(position_list) > len(position_set):
            return True
        else:
            return False