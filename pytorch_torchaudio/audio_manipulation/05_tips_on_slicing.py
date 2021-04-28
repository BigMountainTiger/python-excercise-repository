import requests
import torchaudio

def run():
  SAMPLE_WAV_SPEECH_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/VOiCES_devkit/source-16k/train/sp0307/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav"
  
  # Fetch and decode the 1 - 2 seconds
  frame_offset, num_frames = 16000, 16000

  print("Fetching all the data...")
  with requests.get(SAMPLE_WAV_SPEECH_URL, stream=True) as response:
    waveform1, sample_rate1 = torchaudio.load(response.raw)
    waveform1 = waveform1[:, frame_offset:frame_offset+num_frames]
    print(f" - Fetched {response.raw.tell()} bytes")

  print("Fetching until the requested frames are available...")
  with requests.get(SAMPLE_WAV_SPEECH_URL, stream=True) as response:
    waveform2, sample_rate2 = torchaudio.load(
        response.raw, frame_offset=frame_offset, num_frames=num_frames)
    print(f" - Fetched {response.raw.tell()} bytes")

  print("Checking the resulting waveform ... ", end="")
  assert (waveform1 == waveform2).all()
  print("matched!")

if __name__ == '__main__':
  run()