# pip install -q torchaudio omegaconf soundfile

import torch
import zipfile
import torchaudio
from glob import glob

def run():
  device = torch.device('cpu')

  model, decoder, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-models',
    model='silero_stt',
    language='en',
    device=device
  )

  print('Done')

if __name__ == '__main__':
  run()