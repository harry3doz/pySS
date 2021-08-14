import wave as wave
import numpy as np
import matplotlib.pyplot as plt


sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"

wav = wave.open(sample_wave_file)
data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

# normalize data value
data = data/np.iinfo(np.int16).max

# value of x axis
x = np.array(range(wav.getnframes())) / wav.getframerate()

# plot sound data
plt.figure(figsize=(10, 4))
plt.xlabel("Time [sec]")
plt.ylabel("Value [-1, 1]")
plt.plot(x, data)

# save as .png image
plt.savefig("./wave_form.png")

# display
plt.show()