import torch
import torchaudio
import torchaudio.functional as F
import torchaudio.transforms as T

def verify():
  print(torch.__version__)
  print(torchaudio.__version__)

if __name__ == '__main__':
  verify()