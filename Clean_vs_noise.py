#Finding the jitter difference between a clean sound file and the same file with white noise.
#(This is just for one file, below it is explained for multiple files at different noise levels)
#For sound a :
import matplotlib.pyplot as plt
import numpy as np
import math
import soundfile
import os
import librosa
import parselmouth
from parselmouth.praat import call

#calculating jitter percentage for a clean sound file
file_name = r'/home/kruthika/Desktop/sound e.wav' 
sound = parselmouth.Sound(file_name)
pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
jitter_percentage = call(pointprocess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
jitter_percentage
 (0.005479055843300457)

#creating a sound file with noise
signal, sr = librosa.load(file_name, sr = 16000)
RMS=math.sqrt(np.mean(signal**2))
STD_n= 0.001
noise=np.random.normal(0, STD_n, signal.shape[0])
signal_noise = signal+noise
soundfile.write('filename.wav',signal_noise,16000)

#calculating jitter for sound file with noise
file = r'/home/kruthika/filename.wav'
sound = parselmouth.Sound(file)
pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
jitter_percentage = call(pointprocess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
jitter_percentage
  (0.005501534763533869)

#Here as we can observe, the change in percentage between the two is 0.0022%

#For sound e :
#Similarly, when i calculated the jitter measures for the sound e of my voice, with and without noise the change in jitter percentage I observed was : 0.0038%
