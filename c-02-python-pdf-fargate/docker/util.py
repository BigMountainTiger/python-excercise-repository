import time
import datetime
import os
import glob
import subprocess
import boto3

# clearDirectory
def clearDirectory(directory):
  files = glob.glob(f'{directory}*')
  for f in files:
    os.remove(f)

# docx_replace
def docx_replace(doc, regex, replace):

  for p in doc.paragraphs:
    if regex.search(p.text):
      inline = p.runs
      for i in range(len(inline)):
        if regex.search(inline[i].text):
          text = regex.sub(replace, inline[i].text)
          inline[i].text = text

  for table in doc.tables:
    for row in table.rows:
      for cell in row.cells:
        docx_replace(cell, regex, replace)

def docx_test_table(doc):
  pass

# doc2pdf
def doc2pdf(word_file, result_path):  
  # cmd = f'libreoffice --convert-to pdf {word_file} --outdir {result_path}'.split()
  cmd = f'abiword --to=pdf {word_file}'.split()
  p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  p.wait()
  stdout, stderr = p.communicate()


def upload2s3(bucket, result_pdf_file):
  ts = datetime.datetime.fromtimestamp(time.time()).strftime(r'%Y-%m-%d-%H-%M-%S')
  object_name = f'G-{ts}.pdf'

  s3 = boto3.resource('s3')
  s3.meta.client.upload_file(result_pdf_file, bucket, object_name)
