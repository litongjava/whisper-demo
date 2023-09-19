import sounddevice as sd
import numpy as np

# 设置参数
duration = 5  # seconds
sample_rate = 44100  # Hz

print("Recording for {} seconds...".format(duration))
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.float32)
sd.wait()

print("Playing back the recorded audio...")
sd.play(audio_data, samplerate=sample_rate)
sd.wait()

print("Done!")
