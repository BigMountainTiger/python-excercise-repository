import os
import torchaudio

def _get_sample(path, resample=None):
  effects = [
    ["remix", "1"]
  ]
  if resample:
    effects.append(["rate", f'{resample}'])
  return torchaudio.sox_effects.apply_effects_file(path, effects=effects)

def get_sample(*, resample=None):
  _SAMPLE_DIR = "_sample_data"
  SAMPLE_WAV_PATH = os.path.join(_SAMPLE_DIR, "steam.wav")
  return _get_sample(SAMPLE_WAV_PATH, resample=resample)

def print_stats(waveform, sample_rate=None, src=None):
  if src:
    print("-" * 10)
    print("Source:", src)
    print("-" * 10)
  if sample_rate:
    print("Sample Rate:", sample_rate)
  print("Shape:", tuple(waveform.shape))
  print("Dtype:", waveform.dtype)
  print(f" - Max:     {waveform.max().item():6.3f}")
  print(f" - Min:     {waveform.min().item():6.3f}")
  print(f" - Mean:    {waveform.mean().item():6.3f}")
  print(f" - Std Dev: {waveform.std().item():6.3f}")
  print()
  print(waveform)
  print()

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

def inspect_file(path):
  print("-" * 10)
  print("Source:", path)
  print("-" * 10)
  print(f" - File size: {os.path.getsize(path)} bytes")
  print_metadata(torchaudio.info(path))

def run():
  waveform, sample_rate = get_sample()
  print_stats(waveform, sample_rate=sample_rate)

  path = "save_example_default.wav"
  torchaudio.save(path, waveform, sample_rate)
  inspect_file(path)

  # File is removed after testing
  os.remove(path)

  path = "save_example_PCM_S16.wav"
  torchaudio.save(
    path, waveform, sample_rate,
    encoding="PCM_S", bits_per_sample=16)
  inspect_file(path)

  # File is removed after testing
  os.remove(path)

  # Save to different format
  formats = [
    "mp3",
    "flac",
    "vorbis",
    "sph",
    "amb",
    "amr-nb",
    "gsm",
  ]

  for format in formats:
    path = f"save_example.{format}"
    torchaudio.save(path, waveform, sample_rate, format=format)
    inspect_file(path)

    os.remove(path)

  # Saving to Bytes buffer
  buffer_ = io.BytesIO()
  torchaudio.save(buffer_, waveform, sample_rate, format="wav")

  buffer_.seek(0)
  print(buffer_.read(16))

if __name__ == '__main__':
  run()