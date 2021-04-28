import os
import requests

import torch
import torchaudio
import tarfile
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import matplotlib.pyplot as plt

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

def run():

  SAMPLE_WAV_SPEECH_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/VOiCES_devkit/source-16k/train/sp0307/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav"
  with requests.get(SAMPLE_WAV_SPEECH_URL, stream=True) as response:
    waveform, sample_rate = torchaudio.load(response.raw)
  plot_specgram(waveform, sample_rate, title="HTTP datasource")

  _SAMPLE_DIR = "_sample_data"
  SAMPLE_TAR_PATH = os.path.join(_SAMPLE_DIR, "sample.tar.gz")
  SAMPLE_TAR_ITEM = "VOiCES_devkit/source-16k/train/sp0307/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav"
  with tarfile.open(SAMPLE_TAR_PATH, mode='r') as tarfile_:
    fileobj = tarfile_.extractfile(SAMPLE_TAR_ITEM)
    waveform, sample_rate = torchaudio.load(fileobj)
  plot_specgram(waveform, sample_rate, title="TAR file")

  S3_BUCKET = "pytorch-tutorial-assets"
  S3_KEY = "VOiCES_devkit/source-16k/train/sp0307/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav"
  client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
  response = client.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
  waveform, sample_rate = torchaudio.load(response['Body'])
  plot_specgram(waveform, sample_rate, title="From S3")

if __name__ == '__main__':
  run()