from functools import partial
from tkinter import *
from PIL import ImageTk, Image
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
        img = ImageTk.PhotoImage(Image.open(self.image))

        self.mainwindow.title(self.title)

        imagePanel = Label(self.mainwindow, image=img)

        # imagePanel.pack(side=LEFT, fill="both")

        for i in range(len(self.buttons)):
            self.buttons[i] = Button(self.mainwindow, text=self.buttons[i], bg="Orange", bd=6, activebackground="Grey",
                                     height=2, width=5,
                                     command=partial(self.play_sound, self.sounds[i]))
            self.buttons[i].pack(side=TOP, expand="yes")

    def play_sound(self, sound):
        sd.play(sound)
        # status = sd.wait()

    def show_gui(self):
        self.mainwindow.mainloop()
