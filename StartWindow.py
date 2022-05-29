import gi, random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GObject
from AdditionalInfo import AdditionalInfo

from GameLevel import GameLevel
from GameWindow import GameWindow
import cairo


class StartWindow(Gtk.Window):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.set_title("Brick Breaker")
        self.set_size_request(800, 800)
        self.create_menu_bar()
        self.show_game_window_flag = True

    def create_menu_bar(self):
        self.vbox = Gtk.VBox(False, 1)
        self.add(self.vbox)

        menu_bar = Gtk.MenuBar()

        menu = Gtk.Menu()
        start_game = Gtk.MenuItem("Rozpocznij grę")
        start_game.set_submenu(menu)
        start = Gtk.MenuItem("Start")
        start.connect("activate", self.show_game_window)
        menu.append(start)
        menu_bar.append(start_game)

        menu = Gtk.Menu()
        additional_info = Gtk.MenuItem("Informacje dodatkowe")
        additional_info.set_submenu(menu)
        about_application = Gtk.MenuItem("Opis aplikacji")
        about_application.connect("activate", self.show_additional_info_box)
        menu.append(about_application)
        menu_bar.append(additional_info)

        menu = Gtk.Menu()
        end_game = Gtk.MenuItem("Koniec gry")
        end_game.set_submenu(menu)
        end = Gtk.MenuItem("Wyjście")
        end.connect("activate", self.end_game)
        menu.append(end)
        menu_bar.append(end_game)

        self.vbox.pack_start(menu_bar, False, False, 0)

    def show_game_window(self, _):
        if self.show_game_window_flag == True:
            self.show_game_window_flag = False
            self.game_window = GameWindow()
            self.game_window.connect("delete-event", Gtk.main_quit)
            self.game_window.show_all()
            Gtk.main()


    def show_additional_info_box(self, _):
        dialog = AdditionalInfo(self)
        dialog.run()
        dialog.destroy()

    def end_game(self, _):
        self.destroy()
        self.game_window.destroy()
