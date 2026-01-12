from flask import Flask, request, jsonify
import torch, torchaudio
from glob import glob

import threading
import os

lock = threading.Lock()
device = torch.device('cpu')
load_local_model = False
(model, decoder, utils) = torch.hub.load(repo_or_dir = 'snakers4/silero-models'
    if not load_local_model
    else '/home/song/.cache/torch/hub/snakers4_silero-models_master', 
    model = 'silero_stt',
    source = 'local' if load_local_model else 'github',
    device = device,
    force_reload = False
  )
(read_batch, split_into_batches, read_audio, prepare_model_input) = utils

def identify():
  test_file = 'download/recording.wav'

  test_files = glob(test_file)
  batches = split_into_batches(test_files, batch_size = 1)
  input = prepare_model_input(read_batch(batches[0]), device = device)

  with lock:
    output = model(input)

  results = []
  for r in output:
    results.append(decoder(r.cpu()).strip())

  return ''.join(results)

app = Flask(__name__)
@app.route('/')
def message():
  result = identify()
  return jsonify(
    id = result
  )
    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000, debug=False, threaded=True)