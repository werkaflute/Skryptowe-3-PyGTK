import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from GameLevel import GameLevel


class Game:
    def __init__(self):
        self.level_1 = GameLevel(1)
        self.level_2 = GameLevel(2)
        self.game_level = self.level_1

    def start_game(self):
        if self.game_level.level_2 == True:
            self.game_level = self.level_2
        if self.game_level.level_number <= 2:
            self.game_level.start_game()