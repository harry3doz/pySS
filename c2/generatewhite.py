import wave as wave
import numpy as np
import matplotlib.pyplot as plt

# set the number of samples
n_sample = 40000

# set sampling frequency
sample_rate = 16000

# set random seed
np.random.seed(0)

# generate white noise
data = np.random.normal(size=n_sample)

# the value of x axis
x = np.array(range(n_sample)) / sample_rate

# plot
plt.figure(figsize=(10,4))
plt.xlabel("Time [sec]")
plt.ylabel("Value")
plt.plot(x, data)

# save as .png image
plt.savefig("./whitenoise.png")

# display
plt.show()