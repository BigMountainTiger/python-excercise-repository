import os
import re
from docx import Document
import util

def merge():
  result_directory = './result/'
  fileName = 'result'
  result_word_file = f'{result_directory}{fileName}.docx'
  result_pdf_file = f'{result_directory}{fileName}.pdf'
  template = './template/invoice-template.docx'
  bucket = 'logs.huge.head.li'
  replacement = os.environ.get('REPLACEMENT', r'Paul Kempa')

  # Clear the result directory
  util.clearDirectory(result_directory)

  # Create the new word document
  wdoc = Document(template)
  util.docx_replace(wdoc, re.compile(r'{{customername}}') , replacement)
  wdoc.save(result_word_file)

  # Convert to PDF
  util.doc2pdf(result_word_file, result_directory)

  # Upload to S3
  util.upload2s3(bucket, result_pdf_file)

  print('Completed')

if __name__ == '__main__':
  merge()