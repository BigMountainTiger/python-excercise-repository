# pip install -q torchaudio omegaconf soundfile

import torch
# import zipfile
import torchaudio
from glob import glob

def run():
  device = 'cuda' if torch.cuda.is_available() else 'cpu'
  (model, decoder, utils) = torch.hub.load(repo_or_dir = 'snakers4/silero-models', model = 'silero_stt', language = 'en', device = device)

  (read_batch, split_into_batches, read_audio, prepare_model_input) = utils

  # test_file = 'download/speech_orig.wav'
  # wav_url = 'https://opus-codec.org/static/examples/samples/speech_orig.wav'
  # torch.hub.download_url_to_file(wav_url, dst = test_file, progress = True)

  test_file = 'download/Recording.wav'

  test_files = glob(test_file)
  batches = split_into_batches(test_files, batch_size = 10)
  input = prepare_model_input(read_batch(batches[0]), device = device)
  output = model(input)

  print("\nThis is the result")
  for example in output:
    print(decoder(example.cpu()))

  print('Done')

if __name__ == '__main__':
  run()