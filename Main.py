import threading
import time
import keyboard
import numpy as np
import sounddevice as sd

from GUI import GraphicalUserInterface
from String import GuitarString


class PlaybackThread(threading.Thread):
    def __init__(self, sound, key):
        threading.Thread.__init__(self)
        self.sound = sound
        self.key = key
        # self.daemon = True

    def run(self):
        while True:
            try:
                if keyboard.is_pressed(self.key):  # if key 'q' is pressed
                    self.play()
                time.sleep(0.1)
            except:
                print("error")
                break

    def play(self):
        sd.play(self.sound)
        status = sd.wait()


image = "guitar_design.png"
frequencies = [55, 58, 62, 65, 69, 73, 78, 82, 87, 92, 98, 104]
buttons = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
sampling_frequency = 48000

string_objects = []
sounds = []

for i in frequencies:
    guitar_string = GuitarString(i, sampling_frequency, 1.2)
    guitar_string.karplus_strong_algorithm()
    string_objects.append(guitar_string)

for i in string_objects:
    sounds.append(np.array(i.get_string()))

gui = GraphicalUserInterface(sounds, image, buttons, "Guitar synthesizer")

gui.show_gui()


"""
for i in range(len(buttons)):
    t = PlaybackThread(sounds[i], buttons[i])
    t.start()

print("done")
"""
