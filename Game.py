import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


from GameLevel import GameLevel


class Game:
    def __init__(self, parent):
        self.parent = parent
        self.level_1 = GameLevel(parent, 1)
        self.level_2 = GameLevel(parent, 2)
        self.game_level = self.level_1

    def start_game(self):
        self.game_level.start_game()