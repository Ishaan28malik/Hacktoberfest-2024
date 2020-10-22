import PyPDF2
book = open('d:/Programming/random/audiobook-master/audiobook-master/oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)