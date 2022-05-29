import random
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Ball:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if random.randint(0, 1) == 1:
            self.x_speed = 10
        else:
            self.x_speed = -10
        self.y_speed = -10
        self.ball_under_board = False

    def start_move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x <= 5:
            self.x_speed = -self.x_speed
        if self.y <= 5 :
            self.y_speed = -self.y_speed
        if self.x > 780:
            self.x_speed = -self.x_speed
            self.y_speed = self.y_speed
        if self.y > 800:
            self.ball_under_board = True