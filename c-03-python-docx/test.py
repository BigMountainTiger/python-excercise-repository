# https://python-docx.readthedocs.io/en/latest/user/quickstart.html

import os
import glob
from docx import Document

import util

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

  util.docx_fill_data(wdoc)

  wdoc.save(result_file)

  print('Done')

if __name__ == '__main__':
  test()