import glob
from docx import Document

def clearDirectory(directory):
  files = glob.glob(f'{directory}*')
  for f in files:
    os.remove(f)

def test():
  template_file = './template/invoice-template.docx'
  result_directory = './result/'
  result_file = f'{result_directory}result.docx'

  clearDirectory(result_directory)

  wdoc = Document(template_file)

  wdoc.save(result_file)

  print('Done')

if __name__ == '__main__':
  test()