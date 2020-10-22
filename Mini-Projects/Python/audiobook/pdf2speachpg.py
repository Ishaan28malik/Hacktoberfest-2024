import pyttsx3
import PyPDF2
book = open('d:/Programming/random/audiobook-master/audiobook-master/How to Win Every Argument.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfReader.getPage(12)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
