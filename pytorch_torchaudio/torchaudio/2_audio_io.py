import os
import requests
import torchaudio

_SAMPLE_DIR = "_sample_data"
SAMPLE_WAV_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/steam-train-whistle-daniel_simon.wav"
SAMPLE_WAV_PATH = os.path.join(_SAMPLE_DIR, "steam.wav")
SAMPLE_MP3_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/steam-train-whistle-daniel_simon.mp3"
SAMPLE_MP3_PATH = os.path.join(_SAMPLE_DIR, "steam.mp3")
SAMPLE_GSM_PATH = os.path.join(_SAMPLE_DIR, "steam.gsm")

def print_metadata(metadata, src=None):
  if src:
    print("-" * 10)
    print("Source:", src)
    print("-" * 10)
  print(" - sample_rate:", metadata.sample_rate)
  print(" - num_channels:", metadata.num_channels)
  print(" - num_frames:", metadata.num_frames)
  print(" - bits_per_sample:", metadata.bits_per_sample)
  print(" - encoding:", metadata.encoding)
  print()

def quering_audio_metadata():

  metadata = torchaudio.info(SAMPLE_WAV_PATH)
  print_metadata(metadata, src=SAMPLE_WAV_PATH)

  metadata = torchaudio.info(SAMPLE_MP3_PATH)
  print_metadata(metadata, src=SAMPLE_MP3_PATH)

  metadata = torchaudio.info(SAMPLE_GSM_PATH)
  print_metadata(metadata, src=SAMPLE_GSM_PATH)

def querying_file_like_object():

  with requests.get(SAMPLE_WAV_URL, stream=True) as response:
    metadata = torchaudio.info(response.raw)

  print_metadata(metadata, src=SAMPLE_WAV_URL)

  with requests.get(SAMPLE_MP3_URL, stream=True) as response:
    metadata = torchaudio.info(response.raw, format="mp3")
    print(f"Fetched {response.raw.tell()} bytes.")

  print_metadata(metadata, src=SAMPLE_MP3_URL)

if __name__ == '__main__':

  quering_audio_metadata()
  querying_file_like_object()