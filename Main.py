import numpy as np
import sounddevice as sd

from PIL import Image
from GUI import GraphicalUserInterface
from String import GuitarString

sd.default.latency = 'low'

"""Opening images for GUI"""
back_image = Image.open("guitar_design.jpg")
string_image = Image.open("string.jpg")

frequencies = [55, 62, 65, 73, 82, 87, 98]  # Frequencies of the string notes
buttons = ["A", "B", "C", "D", "E", "F", "G"]  # String notes
sampling_frequency = 44100  # Sampling frequency

"""Lists for storing the synthesized sounds, and string objects"""
string_objects = []
sounds = []

"""Making String objects, and synthesizing the random noise, and appending the objects to the list"""
for i in frequencies:
    guitar_string = GuitarString(i, sampling_frequency, 1.2)
    guitar_string.karplus_strong_algorithm()
    string_objects.append(guitar_string)

"""Retrieving the sounds from the string objects, and appending them to an array"""
"""To pass later that array into GUI Object"""
for i in string_objects:
    sounds.append(np.array(i.get_string()))

"""Creating an object of GUI and passing it the synthesized sounds"""
gui = GraphicalUserInterface(sounds, back_image, string_image, buttons, "Guitar synthesizer")

"""Displaying the GUI"""
gui.show_gui()
