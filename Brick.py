import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Brick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class BrickList:
    def __init__(self, level_number):
        self.level_number = level_number
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        if self.level_number == 1:
            i_range = 10
            j_range = 5
            for i in range(i_range):
                for j in range(j_range):
                    brick = Brick(70 * i + 50, 40 * j + 50, 50, 20)
                    self.bricks.append(brick)

        else:
            i_range = 10
            j_range = 7
            for i in range(i_range):
                for j in range(j_range):
                    if i != 2 and i != 8:
                        brick = Brick(70 * i + 50, 40 * j + 50, 50, 20)
                        self.bricks.append(brick)