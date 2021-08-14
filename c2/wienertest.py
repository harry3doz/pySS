import wave as wave
import numpy as np
import scipy.signal as sp
import sounddevice as sd
import matplotlib.pyplot as plt

sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)

# set speech section 
n_speech = wav.getnframes()
sampling_rate = wav.getframerate()
speech_signal = wav.readframes(wav.getnframes())
speech_signal = np.frombuffer(speech_signal, dtype=np.int16)

# add white noise
np.random.seed(0)
n_noise_only = 40000  # length of noise-only sectionn
n_sample = n_noise_only + n_speech
wgn_signal = np.random.normal(scale=0.04, size=n_sample)
wgn_signal = wgn_signal * np.iinfo(np.int16).max
wgn_signal = wgn_signal.astype(np.int16)  # float --> int16

# mixture
mix_signal = wgn_signal
mix_signal[n_noise_only:,] += speech_signal

# stft
f, t, stft_data = sp.stft(mix_signal, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)

# get amplitude
amp = np.abs(stft_data)
input_power = np.power(amp, 2.0)

# the number of noise-only frames
n_noise_only_frame = np.sum(t < (n_noise_only/sampling_rate))


# =====
# parameters
# =====
alpha = 1.0  
mu = 10
eps = 0.01 * input_power  # not to take less than 1 percent of the input signal amplitude

# estimate power of noise
noise_power = np.mean(np.power(amp,2.0)[:,:n_noise_only_frame], axis=1, keepdims=True)

# calculate power of output signal
processed_power = np.maximum(input_power - alpha*noise_power, eps)
wf_ratio = processed_power / (processed_power + mu*noise_power)
processed_stft_data = wf_ratio * stft_data

# istft
t, processed_data_post = sp.istft(processed_stft_data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)
processed_data_post = processed_data_post.astype(np.int16)

wave_out = wave.open("./wiener_filtered.wav", 'w')
wave_out.setchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(wav.getframerate())
wave_out.writeframes(processed_data_post)

# closing
wave_out.close()

# =====
#  plot subtracted data
# =====
fig = plt.figure(figsize=(10, 4))
spectrum, freqs, t, im = plt.specgram(processed_data_post, NFFT=512, noverlap=512/16*15, Fs=wav.getframerate(), cmap="gray")
fig.colorbar(im).set_label('Intensity [dB]')
plt.xlabel("Time [sec]")
plt.ylabel("Frequency [Hz]")

# save as .png image
plt.savefig("./wiener_filtered_plot.png")

# display
plt.show()

# =====
# plot mixture data
# =====

# stft
t, data_post = sp.istft(stft_data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)
data_post = data_post.astype(np.int16)

# plot
fig = plt.figure(figsize=(10, 4))
spectrum, freqs, t, im = plt.specgram(data_post, NFFT=512, noverlap=512/16*15, Fs=wav.getframerate(), cmap="gray")
fig.colorbar(im).set_label('Intensity [dB]')
plt.xlabel("Time [sec]")
plt.ylabel("Frequency [Hz]")

# save as .png image
plt.savefig("./wiener_mixtured_plot.png")

# display
plt.show()

wave_out = wave.open("./wiener_mixtured.wav", 'w')
wave_out.setchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(wav.getframerate())
wave_out.writeframes(data_post)

wave_out.close()

# closing
wav.close()
