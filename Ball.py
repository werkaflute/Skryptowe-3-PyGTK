import random
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        if random.randint(0, 1) == 1:
            self.x_speed = 7
        else:
            self.x_speed = -7
        self.y_speed = -7
        self.ball_under_board = False

    def start_move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x - self.radius <= 5:
            self.x_speed = -self.x_speed
        if self.y <= 0:
            self.y_speed = -self.y_speed
        if self.x + self.radius > 790:
            self.x_speed = -self.x_speed
            self.y_speed = self.y_speed
        if self.y + self.radius > 800:
            self.ball_under_board = True