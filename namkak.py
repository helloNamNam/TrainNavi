# -*- coding: utf-8 -*-
from Tkinter import*
class Py:
    def __init__ (self):
        self.world = Tk()
        self.world.geometry("800x450")
        self.world.title("Train navigator")

        self.draw = Canvas(self.world,width = 400, height = 200)
        self.draw.pack()

        self.b = Button(self.draw, text = "asdfghfd", command = self.button)
        self.b.grid(row = 0,column = 0 )

        self.b = Button(self.draw, text = "asdfghfd", command = self.button)
        self.b.grid(row = 0,column = 1)


        self.world.mainloop()

    def button(self):
        print("")

Py()
