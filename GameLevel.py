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
        self.score_points = 0
        self.lifes = 3
        self.level_number = level_number
        self.create_game_elements()
        self.show_game_over = False
        self.hide_game_elements = False

    def create_game_elements(self):
        self.block = Block(300, 600, 100, 20)
        self.ball = Ball(320, 570, 12)
        self.brick_list = BrickList(self.level_number)

    def start_game(self):
        self.move_ball()
        block_collision, edge = self.detect_collision(self.ball, self.block)
        if block_collision == True:
            self.change_direction_block()
        brick_collision = False
        index = -1
        edge = 0
        if len(self.brick_list.bricks) == 0:
            if self.level_number == 1:
                self.level_2 = True
            else:
                self.game_over()

        for i in range(len(self.brick_list.bricks)):
            brick = self.brick_list.bricks[i]
            brick_collision, edge = self.detect_collision(self.ball, brick)
            if brick_collision == True:
                index = i
                break

        if brick_collision == True:
            self.change_direction(edge)
            self.remove_brick(index)
            self.score_points += 5

        if self.ball.ball_under_board == True:
            if self.lifes > 0:
                self.ball.ball_under_board = False
                self.start_new_ball()
                self.lifes -= 1
            else:
                self.game_over()

    def change_direction(self, edge):
        if edge == 1:  # TOP
            self.ball.y_speed = -self.ball.y_speed
        elif edge == 2:  # RIGHT
            self.ball.x_speed = -self.ball.x_speed
        elif edge == 3:  # BOTTOM
            self.ball.y_speed = -self.ball.y_speed
        else:
            self.ball.x_speed = -self.ball.x_speed

    def change_direction_block(self):
        self.ball.y_speed = -self.ball.y_speed

    def move_ball(self):
        self.ball.start_move()

    def remove_brick(self, index):
        brick = self.brick_list.bricks[index]
        self.brick_list.bricks.remove(brick)

    def start_new_ball(self):
        self.ball.x = self.block.x + 20
        self.ball.y = self.block.y - 25
        self.ball.y_speed = -self.ball.y_speed

    def game_over(self):
        self.hide_game_elements = True
        self.create_game_over_info()

    def create_game_over_info(self):
        self.show_game_over = True

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