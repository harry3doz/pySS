import wave as wave
import numpy as np
import scipy.signal as sp
import sounddevice as sd

# read sample file
sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)
# read wave data in PCM format
data = wav.readframes(wav.getnframes())
# convert the data to 2-byte strings
data = np.frombuffer(data, dtype=np.int16)

# stft
f, t, stft_data = sp.stft(data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)

# set specific frequency components to zero
stft_data[100:,:] = 0

# istft
t, data_post = sp.istft(stft_data, 
                        fs=wav.getframerate(), 
                        window="hann", 
                        nperseg=512, 
                        noverlap=256)

# convert 2-byte data
data_post = data_post.astype(np.int16)

# playback
sd.play(data_post, wav.getframerate())
print("playback started")

status = sd.wait()

# closing
wav.close()
