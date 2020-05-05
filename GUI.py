from functools import partial
from tkinter import *
from PIL import ImageTk
import sounddevice as sd


class GraphicalUserInterface:
    def __init__(self, sounds, image, buttons, title):
        self.sounds = sounds
        self.image = image
        self.buttons = buttons
        self.title = title
        self.init_setup()

    def init_setup(self):
        self.mainwindow = Tk()
        self.mainwindow.title(self.title)

        img = ImageTk.PhotoImage(self.image)

        imgWidth = img.height()
        imgHeight = img.height()

        imageCanvas = Canvas(width=imgWidth, height=imgHeight)
        imageCanvas.create_image(imgWidth/2, imgHeight/2, image=img,)
        imageCanvas.navInfoImage = img

        imageCanvas.pack(side=TOP)

        for i in range(len(self.buttons)):
            self.buttons[i] = Button(self.mainwindow, text=self.buttons[i], bg="Brown", activebackground="Grey",
                                     height=1, width=100)
            self.buttons[i].place(x = imgWidth/2 + 20, y = imgHeight/2 + i * 30, anchor=CENTER)
            self.buttons[i].config(command=partial(self.play_sound, self.sounds[i]))

    def play_sound(self, sound):
        sd.play(sound)

    def show_gui(self):
        self.mainwindow.mainloop()
