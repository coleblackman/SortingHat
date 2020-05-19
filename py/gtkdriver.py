import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Bubble Sort")
        grid = Gtk.Grid()

        self.button = Gtk.Button(label="Bubble")
        self.button.connect("clicked", self.bubble_sort_invoked)
        self.add(self.button)



    def bubble_sort_invoked(self, widget):
        print("bubbleSortclicked")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
