import wave as wave
import numpy as np
import sounddevice as sd

sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"

wav = wave.open(sample_wave_file)
# read wave data in PCM format
data = wav.readframes(wav.getnframes())
# convert the data to 2-byte strings
data = np.frombuffer(data, dtype=np.int16)

# playback
sd.play(data, wav.getframerate())
print("start playback")

# wait for playback to finish
status = sd.wait()

