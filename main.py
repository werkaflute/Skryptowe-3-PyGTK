#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from StartWindow import StartWindow

if __name__ == "__main__":
    window = StartWindow()
    window.show_all()
    Gtk.main()