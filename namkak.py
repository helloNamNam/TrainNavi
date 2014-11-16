# -*- coding: utf-8 -*-
from Tkinter import*
class Py:
    def __init__ (self):
        self.world = Tk()
        self.world.geometry("800x450")
        self.world.title("Train navigator")

        self.draw = Canvas(self.world,width = 550, height = 450, bg = 'Gray')
        self.draw.pack(side = LEFT)

        self.count = Canvas(self.world, width = 250, height = 450, bg = 'Blue')
        self.count.pack(side = RIGHT)

        self.station = ""
        self.label = Label(self.count, text = self.station, bg = 'Blue')
        self.label.place(x = 100, y = 100)


        self.b = Button(self.draw, text = "click", command = self.button)
        self.b.place(x = 200,y = 100 )


        self.world.mainloop()

    def button(self):
        self.station = "sdfgd"
        self.label = Label(self.count, text = self.station)
        self.label.place(x = 100, y = 100)

Py()
