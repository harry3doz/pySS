import wave as wave
import numpy as np
import scipy.signal as sp

# read sample file
sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)
# read wave data in PCM format
data = wav.readframes(wav.getnframes())
# convert the data to 2-byte strings
data = np.frombuffer(data, dtype=np.int16)

# stft
f, t, stft_data = sp.stft(data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)
print("stft finished. shape is: ", np.shape(stft_data))
print("freq-axis[Hz]:  ", f)
print("time-axis[sec]: ", t)

# closing
wav.close()
