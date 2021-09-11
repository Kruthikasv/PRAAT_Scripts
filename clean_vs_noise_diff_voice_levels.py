#Finding the jitter and shimmer percentage difference between a clean sound file and the same file with white noise at different levels of noise(in dB)(0, 5, 10, 20, 30dB)

#I used the voice samples of my dad’s, my brother’s and mine(total=20 sound files)
#Below is the Clean sound file


#import all required libraries
import glob
import numpy as np
import pandas as pd
import parselmouth
import librosa
import soundfile
import math  
import matplotlib.pyplot as plt
from parselmouth.praat import call
#Function to measure jitter, shimmer percentage of clean sound file
def measurePitch(voiceID, f0min, f0max):
    sound = parselmouth.Sound(voiceID) # read the sound
    pitch = call(sound, "To Pitch", 0.0, f0min, f0max) #create a praat pitch object
    pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)
    localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    localShimmer =  call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    return localJitter, localShimmer
# create lists to put the results
file_list = []
localJitter_list = []
localShimmer_list = []
# Go through all the wave files in the folder and measure pitch
for wave_file in glob.glob("/home/kruthika/Desktop/Audio_files/*.wav"):
    sound = parselmouth.Sound(wave_file)
    file_list.append(wave_file) 
    (localJitter, localShimmer) = measurePitch(sound, 75, 600)
    localJitter_list.append(localJitter)
    localShimmer_list.append(localShimmer)
df = pd.DataFrame(np.column_stack([file_list, localJitter_list, localShimmer_list]),
                               columns=[ 'voiceID','localJitter', 'localShimmer']) 
df = pd.concat([df], axis=1)

#--------------------------------------------------------------------------------------------
#Below is the code to add noise of 30db sound file. 

#Function to add noise
def get_white_noise(sound,SNR) :
    RMS_s=math.sqrt(np.mean(sound**2))
    RMS_n=math.sqrt(RMS_s**2/(pow(10,SNR/10)))
    STD_n=RMS_n
    noise=np.random.normal(0, STD_n, sound.shape[0])
    return noise
# create lists to put the results
file_list = []
noise_list = []
localJitter_list = []
localShimmer_list = []

# Go through all the wave files in the folder and measure jitter%, shimmer%
for wave_file in glob.glob("/home/kruthika/Desktop/Audio_files/*.wav"):
    sound, sr = librosa.load(wave_file, sr = 16000)
    sound=np.interp(sound, (sound.min(), sound.max()), (-1, 1))
    file_list.append(wave_file) 
    noise=get_white_noise(sound,SNR=30)
    sound_noise = sound+noise
    noise_list.append(sound_noise)
    signal= parselmouth.Sound(sound_noise)
    pitch = call(signal, "To Pitch", 0.0, 75, 600) #create a praat pitch object
    pointProcess = call(signal, "To PointProcess (periodic, cc)", 75, 600)
    localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    localShimmer = call([signal, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    localJitter_list.append(localJitter)
    localShimmer_list.append(localShimmer)
df = pd.DataFrame(np.column_stack([file_list, localJitter_list, localShimmer_list]),
                               columns=['sound', 'localJitter', 'localShimmer']) 
df = pd.concat([df], axis=1)
