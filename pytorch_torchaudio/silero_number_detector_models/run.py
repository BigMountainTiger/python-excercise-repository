# https://pytorch.org/hub/snakers4_silero-vad_number/

import torch
torch.set_num_threads(1)
from glob import glob
from pprint import pprint

def run():
  model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad',
                              model='silero_number_detector',
                              force_reload=False)

  (get_number_ts, _, read_audio, _, _) = utils

  files_dir = torch.hub.get_dir() + '/snakers4_silero-vad_master/files'

  wav = read_audio(f'{files_dir}/en_num.wav')
  number_timestamps = get_number_ts(wav, model)

  pprint(number_timestamps)


if __name__ == '__main__':
  run()