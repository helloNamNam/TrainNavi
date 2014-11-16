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
        self.label = Label(self.cal, text = self.station)
        self.label.place(x = 100, y = 100)

    def nextt(self):
        self.draw = Canvas(self.front,width = 550, height = 600, bg = 'Gray')
        self.draw.place(x = 0, y = 0)
        self.bts = Button(self.draw, text = "BTS", command = self.button)
        self.bts.place(x = 80,y = 50 )
        self.mrt = Button(self.draw, text = "MRT", command = self.button)
        self.mrt.place(x = 280,y = 50 )
        self.air = Button(self.draw, text = "SRTET", command = self.button)
        self.air.place(x = 480,y = 50 )
        self.photo = ImageTk.PhotoImage(Image.open("1017545_896593440353899_4808160696530414271_n.jpg"))
        self.photoimpage = self.draw.create_image(400,300, image = self.photo)

        self.cal = Canvas(self.front, width = 250, height = 600, bg = 'Blue')
        self.cal.place(x = 550, y = 0)

        self.station = ""
        self.label = Label(self.cal, text = self.station, bg = 'Blue')
        self.label.place(x = 100, y = 100)






        
Train()
