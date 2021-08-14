import wave as wave
import numpy as np
import matplotlib.pyplot as plt

# read sample file
sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)
# read wave data in PCM format
data = wav.readframes(wav.getnframes())
# convert the data to 2-byte strings
data = np.frombuffer(data, dtype=np.int16)

# plot
fig = plt.figure(figsize=(10, 4))
spectrum, freqs, t, im = plt.specgram(data, 
                                      NFFT=512, 
                                      noverlap=512/16*15, 
                                      Fs=wav.getframerate(), 
                                      cmap="gray"
                                    )
fig.colorbar(im).set_label('Intensity [dB]')  # display colorbar
plt.xlabel("Time [sec]")
plt.ylabel("Frequency [Hz]")

# save as .png image
plt.savefig("./spectrogram.png")

# display
plt.show()

# closing
wav.close()
