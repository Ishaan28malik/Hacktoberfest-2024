#My Password Generator 

from tkinter import *
import pyperclip
import random
root = Tk()
root.geometry("750x350")
root.title("My Calc")
root["bg"]= "black"
passstr = StringVar()
passlen = IntVar()
def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passstr.set(password)
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
Label(root, text="Kartik's Password Generator ",bg="black",fg="white",font="Algerian 20 bold").pack()
Label(root, text="Enter password length",fg="white",bg="black",font="Algerian 12 bold").pack(pady=10)
Entry(root, textvariable=passlen,font=5).pack(pady=8)
Button(root, text="Generate Password",bg="black",fg="white",pady=15,font="Algerian 12", command=generate).pack(pady=7)
Entry(root, textvariable=passstr,font=5).pack(pady=8)
Button(root, text="Copy to clipboard", bg="black",fg="white",pady=15,font="Algerian 12",command=copytoclipboard).pack()
root.mainloop()
