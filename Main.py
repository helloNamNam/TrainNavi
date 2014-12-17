from Tkinter import *
from PIL import Image, ImageTk
class Interface(object):
    """ Interface """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("800x600+400+50")
        self.root.title("Train Navigator")

        #__Background__#
        photo = ImageTk.PhotoImage(Image.open("Image/Train.jpg"))
        bg_inter = Label(self.root, image = photo)
        bg_inter.place(x=0, y=0)

        #__Button__#
        next_but = Button(self.root, text = "Next", command = self.next_method)
        next_but.place(x=650, y=550)

        self.root.mainloop()

    def next_method(self):
        """ call new class """
        self.root.destroy()
        Main()

class Main(object):
    """ main class to select type of travel """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("800x600+400+100")
        self.root.title("Main")

        #__Background and Image__#
        photo = ImageTk.PhotoImage(Image.open("Image/menu.jpg"))
        bts_photo = ImageTk.PhotoImage(Image.open("Train/bts train.jpg"))
        mrt_photo = ImageTk.PhotoImage(Image.open("Train/mrt train.jpg"))
        arl_photo = ImageTk.PhotoImage(Image.open("Train/air train.jpg"))
        bts_but_p = ImageTk.PhotoImage(Image.open("Image/bts b.jpg"))
        mrt_but_p = ImageTk.PhotoImage(Image.open("Image/mrt b.jpg"))
        arl_but_p = ImageTk.PhotoImage(Image.open("Image/air b.jpg"))
        bg_main = Label(self.root, image = photo)
        bts_label = Label(self.root, image = bts_photo)
        mrt_label = Label(self.root, image = mrt_photo)
        arl_label = Label(self.root, image = arl_photo)
        bg_main.place(x=0, y=0)
        bts_label.place(x=30, y=300)
        mrt_label.place(x=270, y=300)
        arl_label.place(x=520, y=300)

        #__Button__#
        bts_but = Button(self.root, bg = "white", image = bts_but_p,
                         command = self.bts_method)
        mrt_but = Button(self.root, bg = "white", image = mrt_but_p,
                         command = self.mrt_method)
        arl_but = Button(self.root, bg = "white", image = arl_but_p,
                         command = self.arl_method)
        bts_but.place(x=100, y=200)
        mrt_but.place(x=350, y=200)
        arl_but.place(x=600, y=200)

        self.root.mainloop()

    def bts_method(self):
        """ call BTS page """
        self.root.destroy()
        Station_bts()

    def mrt_method(self):
        """ call MRT page """
        self.root.destroy()
        Station_mrt()

    def arl_method(self):
        """ call ARL page """
        self.root.destroy()
        Station_arl()

class Station_bts(object):
    """ BTS class to select station """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("800x600+400+100")
        self.root.title("BTS Stations")

        #__Background__#
        photo = ImageTk.PhotoImage(Image.open("Image/BTS.jpg"))
        bg_bts = Label(self.root, image = photo)
        bg_bts.place(x=0, y=0)

        #__Option Menu__#
        self.station_list = ['Bang wa','Wutthakat','Talat Phlu','Pho nimit','Wongwian Yai','Krung Thon Buri',\
                              'Saphan Taksin','Surasak','Chong Nonsi','Sala Daeng','Ratchadamri','Siam(Silom)','National Stadium', \
                              '---Bearing---','Bang Na','Udom Suk','Punnawithi','Bang Chak','On nut','Phra Khanong','Ekkamai','Thong Lo','Phrom Phong',\
                              'Asok','Nana','Phloan Chit','Chit Lom','Siam(Sukumvit)','Ratchathewi','Phaya Thai','Victory Monument','Sanam Pao','Ari','Saphan Khwai','Mo chit']
        self.station_one = StringVar()
        self.station_two = StringVar()
        self.option_sta_one = OptionMenu(self.root, self.station_one, *self.station_list
                                         ).place(x=160, y=8)
        self.option_sta_two = OptionMenu(self.root, self.station_two, *self.station_list
                                         ).place(x=160, y=48)
        self.station_one.set(self.station_list[0])
        self.station_two.set(self.station_list[0])
        label_text1 = Label(self.root, text = "Select station to start", bg = "white"
                            ).place(x=10, y=10)
        label_text2 = Label(self.root, text = "Select station end", bg = "white"
                            ).place(x=10, y=50)

        #__Entry Box__#
        self.result_box = StringVar()
        label_text3 = Label(self.root, text = "Price :").place(x=20, y=130)
        label_text4 = Label(self.root, text = "Baht").place(x=170, y=130)
        Entry(self.root, width = 10, textvariable = self.result_box, bg = "white"
              ).place(x=70, y=128)

        #__Button__#
        self.button_bts = Button(self.root, text = "Confirm", bg = "white",
                                 command = self.bts_money).place(x=150, y=90)
        self.button_back = Button(self.root, text = "Back", bg = "white",
                                  command = self.back_method).place(x=5, y=560)

        self.root.mainloop()

    def bts_money(self):
        """ calculate money """
        train_s = ['Bang wa','Wutthakat','Talat Phlu','Pho nimit','Wongwian Yai','Krung Thon Buri',\
                   'Saphan Taksin','Surasak','Chong Nonsi','Sala Daeng','Ratchadamri','Siam(Silom)','National Stadium']
        train_k = ['---Bearing---','Bang Na','Udom Suk','Punnawithi','Bang Chak','On nut','Phra Khanong','Ekkamai','Thong Lo','Phrom Phong',\
                   'Asok','Nana','Phloan Chit','Chit Lom','Siam(Sukumvit)','Ratchathewi','Phaya Thai','Victory Monument','Sanam Pao','Ari','Saphan Khwai','Mo chit']
        bts = {0:15, 1:15, 2:25, 3:28, 4:31, 5:34, 6:37, 7:42, 8:42, 9:42, 10:42, \
               11:42, 12:42, 13:42, 14:42, 15:42, 16:42, 17:52}
        start = self.station_one.get()
        stop = self.station_two.get()
        if (start in train_s and stop not in train_s) or (start in train_k and stop not in train_k) :
            if start in train_s:
                distance = abs(train_s.index(start) - train_s.index('Siam(Silom)'))
                distance += abs(train_k.index('Siam(Sukumvit)') - train_k.index(stop))
            else:
                distance = abs(train_k.index(start) - train_k.index('Siam(Sukumvit)'))
                distance += abs(train_s.index('Siam(Silom)') - train_s.index(stop))
        else:
            if start in train_s:
                distance = abs(train_s.index(start) - train_s.index(stop))
            else:
                distance = abs(train_k.index(start) - train_k.index(stop))
        if distance >= 17:
            self.result_box.set(bts[17])
        else:
            self.result_box.set(bts[distance])

    def back_method(self):
        """ back to main menu """
        self.root.destroy()
        Main()

class Station_mrt(object):
    """ MRT class to select station """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("800x600+400+100")
        self.root.title("MRT Stations")

        #__Background__#
        photo = ImageTk.PhotoImage(Image.open("Image/Mrt.jpg"))
        bg_mrt = Label(self.root, image = photo)
        bg_mrt.place(x=0, y=0)

        #__Option Menu__#
        self.station_list = ['Hua Lamphong', 'Sam Yan', 'Si Lom', 'Lumphini', 'Khlong Toei', \
                            'Queen Sirikit National Conv Center', 'Phetchburi', 'Phra Ram 9', 'Thailand Cultural Centre', \
                            'Huai Khwang', 'Sutthisan', 'Ratchadaphisek', 'Lat Phrao', 'Phahon Yothin', 'Chatuchak Park', \
                            'Kamphaeng Phet', 'Bang Sue']
        self.station_one = StringVar()
        self.station_two = StringVar()
        self.option_sta_one = OptionMenu(self.root, self.station_one, *self.station_list
                                         ).place(x=150, y=188)
        self.option_sta_two = OptionMenu(self.root, self.station_two, *self.station_list
                                         ).place(x=150, y=228)
        self.station_one.set(self.station_list[0])
        self.station_two.set(self.station_list[0])
        label_text1 = Label(self.root, text = "Select station to start", bg = "#d9fdf9"
                            ).place(x=10, y=188)
        label_text2 = Label(self.root, text = "Select station end", bg = "#d9fdf9"
                            ).place(x=15, y=228)

        #__Entry Box__#
        self.result_box = StringVar()
        Entry(self.root, width = 10, textvariable = self.result_box, bg = "white"
              ).place(x=70, y=308)
        label_text3 = Label(self.root, text = "Price :").place(x=20, y=310)
        label_text4 = Label(self.root, text = "Baht").place(x=170, y=310)

        #__Button__#
        self.button_mrt = Button(self.root, text = "Confirm", bg = "white",
                                 command = self.mrt_money).place(x=140, y=268)
        self.button_back = Button(self.root, text = "Back", bg = "white",
                                  command = self.back_method).place(x=5, y=560)

        self.root.mainloop()

    def mrt_money(self):
        """ calculate money """
        mrt = {0:16, 1:16, 2:18, 3:20, 4:22, 5:25, 6:27, 7:29, 8:31, 9:34, 10:36, 11:38, 12:40}
        first = self.station_list.index(self.station_one.get())
        second = self.station_list.index(self.station_two.get())
        distance = abs(first - second)
        if distance >= 12:
            self.result_box.set(mrt[12])
        else:
            self.result_box.set(mrt[distance])

    def back_method(self):
        """ back to main menu """
        self.root.destroy()
        Main()

class Station_arl(object):
    """ arl class to select station """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("800x600+400+100")
        self.root.title("arl Stations")

        #__Background__#
        photo = ImageTk.PhotoImage(Image.open("Image/Air.jpg"))
        bg_arl = Label(self.root, image = photo)
        bg_arl.place(x=0, y=0)

        #__Option Menu__#
        self.station_list = arl_stationlist = ['Suvarnabhumi', 'Lat Krabang', 'Ban Thap Chang', 'Hua Mak', 'Ramkhamhaeng', 'Makkasan', \
                                              'Ratchaprarop', 'Phaya Thai']
        self.station_one = StringVar()
        self.station_two = StringVar()
        self.option_sta_one = OptionMenu(self.root, self.station_one, *self.station_list
                                         ).place(x=350, y=8)
        self.option_sta_two = OptionMenu(self.root, self.station_two, *self.station_list
                                         ).place(x=350, y=48)
        self.station_one.set(self.station_list[0])
        self.station_two.set(self.station_list[0])
        label_text1 = Label(self.root, text = "Select station to start", bg = "#dafefa"
                            ).place(x=200, y=10)
        label_text2 = Label(self.root, text = "Select station end", bg = "#dafefa"
                            ).place(x=220, y=50)

        #__Entry Box__#
        self.result_box = StringVar()
        Entry(self.root,width = 10,  textvariable = self.result_box, bg = "white"
              ).place(x=250, y=130)
        label_text3 = Label(self.root, text = "Price :").place(x=200, y=132)
        label_text4 = Label(self.root, text = "Baht").place(x=350, y=132)

        #__Button__#
        self.button_arl = Button(self.root, text = "Confirm", bg = "white",
                                 command = self.arl_money).place(x=340, y=90)
        self.button_back = Button(self.root, text = "Back", bg = "white",
                                  command = self.back_method).place(x=5, y=560)

        self.root.mainloop()

    def arl_money(self):
        """ calculate money """
        arl = {0:15, 1:15, 2:20, 3:25, 4:30, 5:35, 6:40, 7:45}
        first = self.station_list.index(self.station_one.get())
        second = self.station_list.index(self.station_two.get())
        distance = abs(first - second)
        self.result_box.set(arl[distance])

    def back_method(self):
        """ back to main menu """
        self.root.destroy()
        Main()
Interface()
        
        
