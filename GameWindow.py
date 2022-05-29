import gi, random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GObject
from Game import Game
import cairo
import math


class GameWindow(Gtk.Window):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.game = Game()
        self.init_ui()
        self.set_title("Brick Breaker")
        self.set_size_request(1300, 800)
        self.connect('key-press-event', self.on_key_press)


    # initialize the Gui
    def init_ui(self):
        self.field = Gtk.DrawingArea()
        self.field.connect("draw", self.on_draw)
        self.field.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.field.queue_draw()
        self.add(self.field)
        self.init_timeout()
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    # draws the field
    def on_draw(self, wid, cr):
        cr.set_line_width(3)
        cr.set_source_rgb(0, 0, 0)
        cr.rectangle(4, 2, 800, 800)
        cr.stroke()
        cr.set_source_rgb(0, 1, 0)
        for i in range(len(self.game.game_level.brick_list.bricks)):
            cr.rectangle(self.game.game_level.brick_list.bricks[i].x, self.game.game_level.brick_list.bricks[i].y,
                         self.game.game_level.brick_list.bricks[i].width, self.game.game_level.brick_list.bricks[i].height)
        cr.fill()
        cr.set_source_rgb(1, 0, 0)
        cr.rectangle(self.game.game_level.block.x, self.game.game_level.block.y,
                     self.game.game_level.block.width, self.game.game_level.block.height)
        cr.fill()
        cr.set_source_rgb(0, 0, 0)
        cr.arc(self.game.game_level.ball.x, self.game.game_level.ball.y, self.game.game_level.ball.radius, 0, 2 * math.pi)
        cr.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL,
                             cairo.FONT_WEIGHT_NORMAL)
        cr.fill()
        cr.set_font_size(13)

        cr.move_to(20, 30)
        cr.show_text("Ilość punktów: " + str(self.game.game_level.ball.x))
        cr.stroke()


    def init_timeout(self):
        GLib.timeout_add(100, self.on_timeout, None)

    def on_timeout(self, *args, **kwargs) -> bool:
        self.start_game_with_level()
        return True

    def start_game_with_level(self):
        if self.game.game_level.level_number == 2:
            None
        self.game.start_game()
        self.field.queue_draw()
        self.add(self.field)

    def on_key_press(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)
        if keyname == 'Left':
            self.game_level.block.move_block(-1)
            self.field.queue_draw()
            self.add(self.field)
        if keyname == 'Right':
            self.game_level.block.move_block(1)
            self.field.queue_draw()
            self.add(self.field)