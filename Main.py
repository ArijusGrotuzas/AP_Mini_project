import threading
import time
import keyboard
import numpy as np
from queue import Queue
import matplotlib.pyplot as plt
import sounddevice as sd
from String import GuitarString

class PlaybackThread(threading.Thread):
    def __init__(self, sound):
        threading.Thread.__init__(self)
        self.sound = sound
        self.daemon = True

    def run(self):
        while True:
            try:
                message = self.queue.get()
                self.play()
            except:
                break

    def play(self):
        sd.play(self.sound)
        status = sd.wait()


frequencies = [55, 58, 62, 65, 69, 73, 78, 82, 87, 92, 98, 104]
sampling_frequency = 48000

string_objects = []
sounds = []

for i in frequencies:
    guitar_string = GuitarString(i, sampling_frequency, 1.2)
    guitar_string.karplus_strong_algorithm()
    string_objects.append(guitar_string)

for i in string_objects:
    sounds.append(np.array(i.get_string()))

thread1 = PlaybackThread(sounds[1])
thread2 = PlaybackThread(sounds[2])
thread3 = PlaybackThread(sounds[3])

thread1.start()
thread2.start()
thread3.start()
"""
for i in sounds:
    sd.play(i)
    status = sd.wait()
"""

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('a'):  # if key 'q' is pressed
            thread1.queue.put("do")

        elif keyboard.is_pressed('s'):
            thread2.queue.put("do")

        elif keyboard.is_pressed('d'):
            thread3.queue.put("do")

    except:
        print("something")