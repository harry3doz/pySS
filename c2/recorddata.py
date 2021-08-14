import wave as wave
import numpy as np
import sounddevice as sd

# recording time[sec]
wave_length = 5

# sampling frequency
sample_rate = 16000

# recording
print("start recording")
data = sd.rec(int(wave_length * sample_rate), sample_rate, channels=1)

# wait for recording to finish
sd.wait()

# adjust scale to write as a form of 2-byte data
data_scale_adjust = data * np.iinfo(np.int16).max
# float --> int16
data_scale_adjust = data_scale_adjust.astype(np.int16)

# write
wave_out = wave.open("./record.wav", 'w')
wave_out.setchannels(1)  # 1: monaural, 2: stereo
wave_out.setsampwidth(2)  # sample size
wave_out.setframerate(sample_rate)
wave_out.writeframes(data_scale_adjust)

# closing
wave_out.close()