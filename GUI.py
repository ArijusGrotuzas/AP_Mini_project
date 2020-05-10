from functools import partial
from tkinter import *
from PIL import ImageTk

from player import AdditiveStream


class GraphicalUserInterface:
    def __init__(self, sounds, image1, image2, buttons, title):
        self.sounds = sounds
        self.image1 = image1
        self.image2 = image2
        self.buttons = buttons
        self.title = title
        self.init_setup()
        self.player = AdditiveStream()

    def init_setup(self):
        color = "#DF9729"

        """Creating the main window"""
        self.mainwindow = Tk()
        self.mainwindow.title(self.title)

        """Opening the passed images"""
        img1 = ImageTk.PhotoImage(self.image1)
        self.img2 = ImageTk.PhotoImage(self.image2)

        """Getting parameters of background image"""
        imgWidth = img1.height()
        imgHeight = img1.height()

        """Variable for updating the current note label"""
        self.var = StringVar()
        self.var.set("")

        """Creating a canvas for displaying background image"""
        imageCanvas = Canvas(width=imgWidth, height=imgHeight, highlightthickness=0)
        imageCanvas.create_image(imgWidth / 2, imgHeight / 2, image=img1)
        imageCanvas.navInfoImage = img1

        imageCanvas.pack(side=TOP)

        """Making a label for current played note"""
        note_label = Label(self.mainwindow, font=("Courier", 25), textvariable=self.var, bg=color)
        note_label.place(x=imgWidth / 2, y=70, anchor=CENTER)

        """Creating buttons and labels, and assigning them sounds and notes"""
        for i in range(len(self.buttons)):
            m = self.buttons[i]
            imageCanvas.create_text(imgWidth / 2, (imgHeight - 40) / 2 + i * 40, text=self.buttons[i], fill="white",
                                    font=("Courier", 15))

            self.buttons[i] = Button(self.mainwindow, bg="grey", activebackground="grey",
                                     image=self.img2, compound=BOTTOM)
            self.buttons[i].place(x=imgWidth / 2, y=imgHeight / 2 + i * 40, anchor=CENTER)
            self.buttons[i].config(command=partial(self.play_sound, self.sounds[i], m))

    def play_sound(self, sound, note):
        self.player.play(sound)  # Adding the sound to the buffer
        self.var.set(note)  # Updating the note label with current sound of the note

    def show_gui(self):
        self.mainwindow.mainloop()  # Starting the main window
