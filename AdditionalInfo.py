import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AdditionalInfo(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Opis aplikacji", transient_for=parent)
        self.add_buttons(Gtk.STOCK_OK, Gtk.ResponseType.OK)

        self.set_default_size(400, 150)

        label = Gtk.Label(label='Gra Brick Breaker \nWykonana na przedmiot "Języki skryptowe i ich zastosowania" \nAutor: Weronika Piotrowska 175771, semestr 1 mgr KASK')

        box = self.get_content_area()
        box.add(label)
        self.show_all()