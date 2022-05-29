import gi, random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GObject
from AdditionalInfo import AdditionalInfo

from GameLevel import GameLevel
import cairo

field_size = 25
win_size = 800
speed = 100



class GameWindow(Gtk.Window):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.game_level = GameLevel(1)
        self.init_ui()
        self.set_title("Brick Breaker")
        self.set_size_request(800, 800)
        self.connect('key-press-event', self.on_key_press)


    # initialize the Gui
    def init_ui(self):
        self.field = Gtk.DrawingArea()
        self.field.connect("draw", self.on_draw)
        self.field.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.field.queue_draw()
        self.add(self.field)
        self.resize(win_size, win_size)

        self.set_position(Gtk.WindowPosition.CENTER)
        self.win_size = self.get_size()
        self.width = self.win_size[1] / field_size

        self.init_timeout()

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    # draws the field
    def on_draw(self, wid, cr):
        cr.set_line_width(1)
        cr.set_source_rgb(1, 0, 0)
        cr.rectangle(self.game_level.block.x, self.game_level.block.y,
                     self.game_level.block.width, self.game_level.block.height)
        cr.rectangle(self.game_level.ball.x, self.game_level.ball.y,
                     self.game_level.ball.width, self.game_level.ball.height)
        cr.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL,
                             cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(13)

        cr.move_to(20, 30)
        cr.show_text("Ilość punktów: " + str(self.game_level.ball.x))
        cr.fill()
        cr.stroke()


    def init_timeout(self):
        # GLib.timeout_add(speed, self.on_timeout, None)
        self.timeout_id = GLib.timeout_add(speed, self.on_timeout, None)
        self.timeout_on = True

    def on_timeout(self, *args, **kwargs) -> bool:
        self.start_game_with_level()
        return True

    def start_game_with_level(self):
        self.game_level.start_game()
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