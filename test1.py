# -*- coding: utf-8 -*-
from Tkinter import*
from PIL import Image, ImageTk
class Py:
    def __init__ (self):
        self.world = Tk()
        self.world.geometry("800x450")
        self.world.title("Train navigator")
        self.photo = ImageTk.PhotoImage(Image.open("10365795_10203253779970891_7349321242957263719_n.gif.jpg"))

        
        self.photoimpage = self.world.create_image(400,225, image = self.photo)



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
        self.station = "สวัสดี"
        self.label = Label(self.count, text = self.station)
        self.label.place(x = 100, y = 100)

Py()
