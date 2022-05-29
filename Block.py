import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move_block(self, direction):
        if direction == -1:
            self.x -= 30
        if direction == 1:
            self.x += 30