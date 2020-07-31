# https://stackoverflow.com/questions/59134487/how-to-generate-a-pdf-with-a-given-template-with-dynamic-data-in-python-or-node
# https://medium.com/@MicroPyramid/generating-pdf-files-in-python-using-xhtml2pdf-34698c63051f
# https://stackoverflow.com/questions/23361810/how-to-change-page-size-in-pdf-generated-by-pisa
# https://stackoverflow.com/questions/3341485/how-to-make-a-html-page-in-a4-paper-size-pages
# https://fwpn.org.pl/assets/event_attachments/asd.html

# xhtml2pdf --css-dump > xhtml2pdf-default.css

import os
import io
import copy
import glob
import time
from xhtml2pdf import pisa 
import jinja2
from PyPDF2 import PdfFileMerger, PdfFileReader

templateLoader = jinja2.FileSystemLoader(searchpath = './')

templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = 'template/invoice.html'
template = templateEnv.get_template(TEMPLATE_FILE)

body = {
    'data':{
        'order_id': 123,
        'order_creation_date': '2020-01-01 14:14:52',
        'company_name': 'Monster LG',
        'city': 'Ellicott City',
        'state': 'MD',
    }
}

sourceHtml = template.render(d=body['data'])
outoutputFolder = './pdf-files/'
outputFilename = outoutputFolder + 'invoice.pdf'

def clearPdf():
  files = glob.glob(outoutputFolder + '*')
  for f in files:
      os.remove(f)

def convertHtmlToPdf(sourceHtml, outputFilename):
    with open(outputFilename, 'w+b') as resultFile:
      pisaStatus = pisa.CreatePDF(src=sourceHtml, dest=resultFile)

    #print(pisaStatus.err, type(pisaStatus.err))
    return pisaStatus.err

def convertHtmlToPdf_stream(sourceHtml, i):
    f_stream = io.BytesIO()
    data = copy.deepcopy(body)
    
    order_id = i + 1
    data['data']['order_id'] = order_id
    data['data']['company_name'] = data['data']['company_name'] + ' ' + str(order_id)
    sourceHtml = template.render(d=data['data'])
    pisaStatus = pisa.CreatePDF(src = sourceHtml, dest = f_stream)

    return f_stream

def convertAll():
  start_time = time.time()

  merger = PdfFileMerger()
  for i in range(10):
      pdf_file = outoutputFolder + 'invoice-' + str(i) + '.pdf';
      convertHtmlToPdf(sourceHtml, pdf_file)
      merger.append(PdfFileReader(pdf_file))
      os.remove(pdf_file)

  merger.write(outoutputFolder + 'document-output.pdf')

  print("Completed in %s seconds" % (time.time() - start_time))

def convertAll_by_stream():
  start_time = time.time()

  merger = PdfFileMerger()
  for i in range(2):
      f_stream = convertHtmlToPdf_stream(sourceHtml, i)
      merger.append(f_stream)

  merger.write(outoutputFolder + 'document-output.pdf')

  print("Completed in %s seconds" % (time.time() - start_time))

def mergeAll():
  merger = PdfFileMerger()

  files = glob.glob(outoutputFolder + '*')
  for f in files:
    print(f)
    merger.append(PdfFileReader(f))
    os.remove(f)

  merger.write(outoutputFolder + 'document-output.pdf')


if __name__ == '__main__':
    # pisa.showLogging()
    clearPdf()
    #convertAll()
    convertAll_by_stream()
    # mergeAll()

    

