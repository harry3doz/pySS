import wave as wave
import numpy as np

# set the number of samples
n_sample = 40000

# set sampling frequency
sample_rate = 16000

# set random seed
np.random.seed(0)

# generate white noise
data = np.random.normal(scale=0.1, size=n_sample)

# adjust scale to write as a form of 2-byte data
data_scale_adjust = data * np.iinfo(np.int16).max
# float --> int16
data_scale_adjust = data_scale_adjust.astype(np.int16)

# write
wave_out = wave.open("./whitenoise.wav", 'w')
wave_out.setchannels(1)  # 1: monaural, 2: stereo
wave_out.setsampwidth(2)  # sample size
wave_out.setframerate(sample_rate)
wave_out.writeframes(data_scale_adjust)

# closing
wave_out.close()

