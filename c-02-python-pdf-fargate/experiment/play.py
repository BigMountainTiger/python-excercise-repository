import io, copy
from docx import Document
from docx.enum.text import WD_BREAK

def play():

  with open('./source-file/result.docx', 'rb') as infile:
    template = infile.read()

  end_docx = Document(io.BytesIO(template))
  end_docx.add_page_break()

  for x in range(1, 1000):
    
    wdoc = Document(io.BytesIO(copy.deepcopy(template)))
    wdoc.add_page_break()

    for element in wdoc.element.body:
      end_docx.element.body.append(element)

  end_docx.save('./target-file/target.docx')

  print('Done')

if __name__ == '__main__':
  play()