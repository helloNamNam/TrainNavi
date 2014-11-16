# -*- coding: utf-8 -*-
from Tkinter import*
from PIL import Image, ImageTk
class Train:
    def __init__ (self):
        self.world = Tk()
        self.world.geometry("800x600")
        self.world.title("Train navigator")
        self.photo = ImageTk.PhotoImage(Image.open("1017545_896593440353899_4808160696530414271_n.jpg"))

        self.front = Canvas(self.world, width = 800, height = 600)
        self.front.pack()

        self.photoimpage = self.front.create_image(400,300, image = self.photo)
        self.click = Button(self.front, text = "Next", command = self.nextt)
        self.click.place(x = 700, y = 550)



        self.world.mainloop()

    def button(self):
        self.station = "สวัสดี"
        self.label = Label(self.count, text = self.station)
        self.label.place(x = 100, y = 100)

    def nextt(self):
        self.draw = Frame(self.front,width = 550, height = 600, bg = 'Gray')
        self.draw.place(x = 0, y = 0)
        self.b = Button(self.draw, text = "click", command = self.button)
        self.b.place(x = 200,y = 100 )

        self.count = Frame(self.front, width = 250, height = 600, bg = 'Blue')
        self.count.place(x = 550, y = 0)

        self.station = ""
        self.label = Label(self.count, text = self.station, bg = 'Blue')
        self.label.place(x = 100, y = 100)






        
Train()
