import os
import torch
import torchaudio
import matplotlib.pyplot as plt
from IPython.display import Audio, display

import numpy as np

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

def plot_waveform(waveform, sample_rate, title="Waveform", xlim=None, ylim=None):
  waveform = waveform.numpy()

  num_channels, num_frames = waveform.shape
  time_axis = torch.arange(0, num_frames) / sample_rate

  figure, axes = plt.subplots(num_channels, 1)
  if num_channels == 1:
    axes = [axes]
  for c in range(num_channels):
    axes[c].plot(time_axis, waveform[c], linewidth=1)
    axes[c].grid(True)
    if num_channels > 1:
      axes[c].set_ylabel(f'Channel {c+1}')
    if xlim:
      axes[c].set_xlim(xlim)
    if ylim:
      axes[c].set_ylim(ylim)
  figure.suptitle(title)
  plt.show(block=True)

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

def plot_specgram(waveform, sample_rate, title="Spectrogram", xlim=None):
  waveform = waveform.numpy()

  num_channels, num_frames = waveform.shape
  time_axis = torch.arange(0, num_frames) / sample_rate

  figure, axes = plt.subplots(num_channels, 1)
  if num_channels == 1:
    axes = [axes]
  for c in range(num_channels):
    axes[c].specgram(waveform[c], Fs=sample_rate)
    if num_channels > 1:
      axes[c].set_ylabel(f'Channel {c+1}')
    if xlim:
      axes[c].set_xlim(xlim)
  figure.suptitle(title)
  plt.show(block=True)

def play_audio(waveform, sample_rate):
  waveform = waveform.numpy()

  num_channels, num_frames = waveform.shape
  if num_channels == 1:
    display(Audio(waveform[0], rate=sample_rate))
  elif num_channels == 2:
    display(Audio((waveform[0], waveform[1]), rate=sample_rate))
  else:
    raise ValueError("Waveform with more than 2 channels are not supported.")
  
def run():

  waveform1, sample_rate1 = get_sample(resample=16000)

  effects = [
    ["lowpass", "-1", "300"], 
    ["speed", "0.8"],
    ["rate", f"{sample_rate1}"],
    ["reverb", "-w"]
  ]

  waveform2, sample_rate2 = torchaudio.sox_effects.apply_effects_tensor(
    waveform1, sample_rate1, effects)

  plot_waveform(waveform1, sample_rate1, title="Original", xlim=(-0.1, 3.2))
  plot_waveform(waveform2, sample_rate2, title="Effects Applied", xlim=(-0.1, 3.2))
  print_stats(waveform1, sample_rate=sample_rate1, src="Original")
  print_stats(waveform2, sample_rate=sample_rate2, src="Effects Applied")

  plot_specgram(waveform1, sample_rate1, title="Original", xlim=(-0.1, 3.2))
  play_audio(waveform1, sample_rate1)
  plot_specgram(waveform2, sample_rate2, title="Effects Applied", xlim=(-0.1, 3.2))
  play_audio(waveform2, sample_rate2)

if __name__ == '__main__':
  run()