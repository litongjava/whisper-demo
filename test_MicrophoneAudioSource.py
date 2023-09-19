import time

from diart.sources import MicrophoneAudioSource

# Initialize the microphone audio source with a sample rate of 16000
sample_rate = 16000
source = MicrophoneAudioSource(sample_rate)


# Define a callback to handle the audio data
def audio_callback(audio_data):
    # For now, just print the length of the audio data
    print(f"Received {len(audio_data)} samples")


# Set up the callback
source.stream.subscribe(audio_callback)

# Read from the microphone for 5 seconds
print("Reading audio...")
time.sleep(5)
print("Finished reading.")

# Note: Depending on the implementation of MicrophoneAudioSource, you might need to stop the source manually.
