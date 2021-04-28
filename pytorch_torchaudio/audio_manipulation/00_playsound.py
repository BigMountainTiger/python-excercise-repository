# from playsound import playsound
import simpleaudio as sa

def run():
  PATH = '_sample_data/stupid.wav'
  # playsound(PATH)

  wave_obj = sa.WaveObject.from_wave_file(PATH)
  play_obj = wave_obj.play()
  play_obj.wait_done()

  print('Done')

if __name__ == '__main__':
  run()