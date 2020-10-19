from tkinter import *
import pyttsx3 as pt
import webbrowser as wb
import os

# -------------------------------------------------------------------------------------
# Speech Engine
engine = pt.init()
def Say(speech):
	engine.say(speech)
	engine.runAndWait()
# -------------------------------------------------------------------------------------

def openweblink(link): # For opening websites
	try:
		wb.open(link)
	except Exception as e:
		print("An Error occured while opening the webpage")
		Say("An Error occured while opening the webpage")

def openfiles(path):
	try:
		os.startfile(path)
	except Exception as e:
		Say("Sorry can't open the file please check the location")

def cmd(): # function to hold the conditions
	order = entry.get().lower()
	if "hello" in order:
		# alabel = Label(root, text="Hello, Sir")
		# alabel.pack()
		print("Hello, Sir")
		Say("Hello, Sir")
	elif "open github" in order:
		print("Opening Github....")
		Say("Opening Github")
		openweblink("https://github.com")
	elif "open sublime" in order:
		Say("Starting Sublime Text")
		openfiles("") # Add your editor location
	elif "quit" in order:
		Say("See you soon sir")
		quit()
	else:
		print("Sorry can't understand your words")
		Say("Sorry can't understand your words")

# GUI of the program
root = Tk()
root.geometry("300x300") # Size of the tkinter window
root.title("Zira v2.0") # Title of the tkinter window
root.minsize(200, 200)
mainText = Label(root, text="Zira - Your Virtual Assistant") # Main Head Text of the Tkinter Window
mainText.pack()

entry = Entry(root) # Takes input of command
entry.pack()

enterBtn = Button(root, text="Enter", command=cmd) # Button to submit
enterBtn.pack()

quitBtn = Button(root, text="Quit", command=quit)
quitBtn.pack()

root.mainloop()
