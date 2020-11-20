import os
import glob
import subprocess

# clearDirectory
def clearDirectory(directory):
  files = glob.glob(f'{directory}*')
  for f in files:
    os.remove(f)

# docx_replace
def docx_replace(doc, regex , replace):
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
        docx_replace(cell, regex , replace)

# doc2pdf
def doc2pdf(word_file, result_path):  
  cmd = f'libreoffice --convert-to pdf {word_file} --outdir {result_path}'.split()
  p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  p.wait()
  stdout, stderr = p.communicate()