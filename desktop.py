# -*- coding: utf-8 -*-
from Tkinter import*
from PIL import Image, ImageTk
class Train:
    def __init__ (self):
        self.world = Tk()
        self.world.geometry("800x600")
        self.world.title("Train navigator")
        self.photo = ImageTk.PhotoImage(Image.open("Triannnn.jpg"))
        self.trainnavi = ImageTk.PhotoImage(Image.open("TrainNavi.jpg"))

        self.front = Canvas(self.world, width = 800, height = 600)
        self.front.pack()

        self.photoimpage = self.front.create_image(400,300, image = self.photo)
        self.phototrainnavi = self.front.create_image(450,500, image = self.trainnavi)
        self.click = Button(self.front, text = "Next", command = self.nextt)
        self.click.place(x = 650, y = 550)



        self.world.mainloop()

   

    def nextt(self):

        self.draw = Canvas(self.front,width = 600, height = 600, bg = 'Gray')
        self.draw.place(x = 0, y = 0)
        
        self.cal = Canvas(self.front, width = 200, height = 600, bg = 'Blue')
        self.cal.place(x = 600, y = 0)


        self.bts = Button(self.draw, text = "BTS", command = self.bts)
        self.bts.place(x = 80,y = 50 )
        self.mrt = Button(self.draw, text = "MRT", command = self.mrt)
        self.mrt.place(x = 320,y = 50 )
        self.air = Button(self.draw, text = "SRTET", command = self.air)
        self.air.place(x = 480,y = 50 )

        
        self.photoBTS = ImageTk.PhotoImage(Image.open("BTS.jpg"))
        self.photoimpage = self.draw.create_image(300,300, image = self.photoBTS, tag = "bts")
        self.draw.tag_raise("bts")

        self.photoMRT = ImageTk.PhotoImage(Image.open("MRT.jpg"))
        self.photoimpage = self.draw.create_image(300,300, image = self.photoMRT, tag = "mrt")
        self.draw.tag_lower("mrt")

        self.photoAIR = ImageTk.PhotoImage(Image.open("AIR.jpg"))
        self.photoimpage = self.draw.create_image(300,300, image = self.photoAIR, tag = "air")
        self.draw.tag_lower("air")
        
        self.station = ""
        self.label = Label(self.cal, text = self.station, bg = 'Blue')
        self.label.place(x = 100, y = 100)


    def bts(self):
        self.station = "สวัสดี"
        self.label = Label(self.cal, text = self.station)
        self.label.place(x = 100, y = 100)
        self.draw.tag_raise("bts")
        self.draw.tag_lower("mrt")
        self.draw.tag_lower("air")

    def mrt(self):
        self.draw.tag_lower("bts")
        self.draw.tag_raise("mrt")
        self.draw.tag_lower("air")

    def air(self):
        self.draw.tag_lower("bts")
        self.draw.tag_lower("mrt")
        self.draw.tag_raise("air")
        






        
Train()
