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

# stft --> istft
f, t, stft_data = sp.stft(data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)
t, data_post = sp.istft(stft_data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)

# convert to 2-byte data
data_post = data_post.astype(np.int16)

# write file
wave_out = wave.open("./istft_post_wave.wav", "w")
wave_out.setchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(wav.getframerate())
wave_out.writeframes(data_post)

# closing
wave_out.close()
wav.close()
