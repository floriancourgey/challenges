#! /usr/bin/env python3
# coding: utf-8
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import *
from functions import *

import numpy as np
from scipy.io import wavfile
from scipy.fft import fft

AMPLITUDE_THRESHOLD = 0.8
FREQUENCY_MULTIPLE = 10

def download_wav():
    response = get(URLS['prog']['wav']['problem'], True)
    with open('sound.wav', 'wb') as file:
        file.write(response.content)

def analyze_frequency(filename):
    # Read the WAV file.
    samplerate, data = wavfile.read(filename)
    # Assume the file is mono for simplicity
    if len(data.shape) > 1:
        data = data[:, 0]

    # Normalize by the maximum
    data = data / np.abs(data).max()

    # Apply Fourier transform
    freqs = fft(data)

    # Get the absolute values to find the magnitude
    spectrum = np.abs(freqs)[:len(freqs)//2]

    # Find the frequency with the highest magnitude
    peak_frequency = np.argmax(spectrum) * (samplerate / len(data))

    # Round to the nearest multiple of 10
    peak_frequency = round(peak_frequency / FREQUENCY_MULTIPLE) * FREQUENCY_MULTIPLE

    return peak_frequency

# Main process
download_wav()
frequency = analyze_frequency('sound.wav')
print(get(URLS['prog']['wav']['solution']+'?freq='+str(frequency)))
