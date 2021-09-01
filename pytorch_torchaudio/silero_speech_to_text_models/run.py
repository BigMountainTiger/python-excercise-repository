# pip install -q torchaudio omegaconf soundfile
# It is pretty accurate to recognize numbers

import torch
# import zipfile
import torchaudio
# torchaudio.set_audio_backend("sox_io")
from glob import glob
from pydub import AudioSegment
import io

def run():
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

  load_local_model = True

  # https://pytorch.org/docs/stable/hub.html
  (model, decoder, utils) = torch.hub.load(repo_or_dir = 'snakers4/silero-models'
      if not load_local_model
      else '/home/song/.cache/torch/hub/snakers4_silero-models_master', 
      model = 'silero_stt',
      source = 'local' if load_local_model else 'github',
      device = device,
      force_reload = True
    )

  (read_batch, split_into_batches, read_audio, prepare_model_input) = utils

  # test_file = 'download/speech_orig.wav'
  # wav_url = 'https://opus-codec.org/static/examples/samples/speech_orig.wav'
  # torch.hub.download_url_to_file(wav_url, dst = test_file, progress = True)

  # def identify():
  #   test_file = 'download/N.wav'

  #   test_files = glob(test_file)
  #   batches = split_into_batches(test_files, batch_size = 10)
  #   input = prepare_model_input(read_batch(batches[0]), device = device)
  #   output = model(input)

  #   print("\nThis is the result")
  #   for example in output:
  #     print(decoder(example.cpu()))

  def identify():
    input = 'download/recording'
    output = 'download/recording.wav'

    ogg_content = None
    with open(input,'rb') as ogg:
      ogg_content = io.BytesIO(ogg.read())

    content = io.BytesIO()

    AudioSegment.from_file(ogg_content).export(content, format="wav")
    with open(output,'wb') as out:
      out.write(content.read())  

    test_files = glob(output)
    batches = split_into_batches(test_files, batch_size = 10)
    input = prepare_model_input(read_batch(batches[0]), device = device)
    output = model(input)

    print("\nThis is the result")
    for example in output:
      print(decoder(example.cpu()))

  identify()
  identify()
  identify()
  identify()
  identify()

  print('Done')

if __name__ == '__main__':
  run()