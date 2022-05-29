import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from Block import Block
from Ball import Ball
from Brick import BrickList
import math


class GameLevel:
    def __init__(self, level_number):
        self.ball = None
        self.block = None
        self.brick_list = None
        self.level_2 = False
        self.level_number = level_number
        self.create_game_elements()

    def create_game_elements(self):
        self.block = Block(300, 600, 100, 20)
        self.ball = Ball(320, 570, 12)
        self.brick_list = BrickList(self.level_number)

    def start_game(self):
        self.move_ball()

    def move_ball(self):
        self.ball.start_move()

    def detect_collision(self, ball, rectangle):
        radius = ball.radius
        cx = ball.x + radius
        cy = ball.y + radius
        testX = cx
        testY = cy
        rx = rectangle.x
        ry = rectangle.y
        rw = rectangle.width
        rh = rectangle.height
        edge = 0
        if cx < rx:
            edge = 4
            testX = rx
        elif cx > rx + rw:
            edge = 2
            testX = rx + rw
        if cy < ry:
            edge = 1
            testY = ry
        elif cy > ry + rh:
            edge = 3
            testY = ry + rh
        distX = cx - testX
        distY = cy - testY
        distance = math.sqrt((distX * distX) + (distY * distY))
        if distance <= radius:
            return True, edge
        else:
            return False, edge