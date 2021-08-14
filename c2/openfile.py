import wave as wave
import pyroomacoustics as pa
import numpy as np

# download CMU ARCTIC Corpus
pa.datasets.CMUArcticCorpus(basedir=".\\CMU_ARCTIC", download=True, speaker=["aew", "axb"])

# read sample file
sample_wave_file = ".\\CMU_ARCTIC\\cmu_us_aew_arctic\\wav\\arctic_a0001.wav"
wav = wave.open(sample_wave_file)

# output information of the file
print("sampling frequency[Hz]: ", wav.getframerate())
print("sample size[Byte]: ", wav.getsampwidth())
print("the number of sample frames: ", wav.getnframes())
print("the number of channels: ", wav.getnchannels())

# read wave data in PCM format
data = wav.readframes(wav.getnframes())

# convert the data to 2-byte strings
data = np.frombuffer(data, dtype=np.int16)

# closing
wav.close()