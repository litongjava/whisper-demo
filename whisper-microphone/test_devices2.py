import numpy as np
import sounddevice as sd

# 设置参数
duration = 5  # seconds
sample_rate = 44100  # Hz
channels = 1  # Mono

# 用于存储录音数据的列表
audio_data_list = []

def callback(indata, frames, time, status):
    """回调函数，将数据添加到audio_data_list"""
    audio_data_list.append(np.frombuffer(indata, dtype=np.int16))

print("Recording for {} seconds...".format(duration))

# 使用 RawInputStream
with sd.RawInputStream(samplerate=sample_rate, channels=channels, dtype='int16', callback=callback):
    sd.sleep(duration * 1000)  # 等待duration秒

# 将多个数组连接成一个
audio_data = np.concatenate(audio_data_list, axis=0)

print("Playing back the recorded audio...")
sd.play(audio_data, samplerate=sample_rate)
sd.wait()

print("Done!")
