# Python program to implement Audiobook Reader

# 1. Read the PDF file
# 2. Initialize Speaker
# 3. Play the Audiobook 

import speech_recognition as sr
import pyttsx3
import PyPDF2

# It will open the pdf in read only mode
book = open('File_Handling_python.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)

# Count the pages of pdf
pages = pdf_reader.numPages
print(pages)

listener = sr.Recognizer()
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
speaker.say('hi how are you!')

for num in range(0,pages) :
    # Get the pages and read it
    page = pdf_reader.getPage(0)

    # Extract the text from pdf
    text = page.extractText()

    # speaker.say('What do you want to speak')
    speaker.say(text)
speaker.runAndWait()