from pydub import AudioSegment
import io

def transform():
  input = 'download/recording.ogx'
  output = 'download/recording.wav'

  content = io.BytesIO()
  AudioSegment.from_file(input).export(content, format="wav")

  with open(output,'wb') as out:
    out.write(content.read())  

if __name__ == '__main__':
  transform()