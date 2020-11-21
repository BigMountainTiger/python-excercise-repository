import re
from docx import Document
import util

def doc2pdf_linux(word_file):  
    cmd = f'libreoffice --convert-to pdf {word_file} --outdir ./result/'.split()
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait(timeout=10)
    stdout, stderr = p.communicate()

def merge():
  result_directory = './result/'
  fileName = 'result'
  result_word_file = f'{result_directory}{fileName}.docx'
  result_pdf_file = f'{result_directory}{fileName}.pdf'
  template = './template/invoice-template.docx'
  bucket = 'logs.huge.head.li'

  # Clear the result directory
  util.clearDirectory(result_directory)

  # Create the new word document
  wdoc = Document(template)
  util.docx_replace(wdoc, re.compile(r'{{customername}}') , r'Paul Kempa')
  wdoc.save(result_word_file)

  # Convert to PDF
  util.doc2pdf(result_word_file, result_directory)

  # Upload to S3
  util.upload2s3(bucket, result_pdf_file)

  print('Completed')

if __name__ == '__main__':
  merge()