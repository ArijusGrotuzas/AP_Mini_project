import numpy as nump


class GuitarString:
    def __init__(self, note_freq, frequency_sample, stretch_factor):
        self.note_freq = note_freq
        self.frequency_sample = frequency_sample
        self.duration = 3 * frequency_sample
        self.stretch_factor = stretch_factor
        self.init_make_wave_form()

    def init_make_wave_form(self):  # For making a random noise wave
        wavetable_size = self.frequency_sample // self.note_freq  # Getting the pitch period of note

        """Generating a random wave based on the pitch period"""
        random_wave = (2 * nump.random.randint(0, 2, wavetable_size) - 1).astype(nump.float)
        self.x = random_wave  # making the local reference to the wave

    def karplus_strong_algorithm(self):
        samples = []  # stores the filtered samples of the waveform
        y = 0  # for keeping the previous value of the waveform

        for j in range(
                self.duration // len(self.x)):  # measures how many times the waveform fits in the length of duration
            for i in range(len(self.x)):  # goes through the length of waveform to sample it
                self.x[i] = 0.5 * (self.x[i] + y)  # y = 0.5 * (x + y-1)
                samples.append(self.x[i])  # appends the sampled value to the end of the current array
                y = samples[
                    len(samples) - 1]  # set the previous sample reference to the current last element in the array

        self.string_sound = nump.array(samples)  # Returns the sound

    def get_string(self):  # For retrieving the sound of string
        return self.string_sound
