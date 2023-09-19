import sounddevice as sd
import wavio

# 参数设置
RATE = 44100  # 采样率
CHANNELS = 1  # 声道数
DURATION = 10  # 录制时长 (秒)

# 录制音频
print("正在录制...")
audio_data = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=CHANNELS, dtype='float32')
sd.wait()  # 等待录制完成
print("录制完成!")

# 保存为 WAV 文件
wavio.write("output.wav", audio_data, RATE, sampwidth=3)
