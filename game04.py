import tkinter
from tkinter import *
import random
from tkinter import messagebox

answer = [
    "python",
    "java",
    "swift",
    "canada",
    "america",
    "india",
    "london",
    "germany",
    "delhi",
    "bhutan",
    "russia",
    "australia",
    "brazil",
    "beijing",
    "mexico",
    "mumbai",
    "tokyo",
    "cairo",
    "japan",
    "france",
    "singapore",
    "iran",
    "indonesia",
    "italy",
    "sweden"
]

word = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdaana",
    "aiearcm",
    "aidin",
    "odnlon",
    "graeynm",
    "dlhei",
    "buahtn",
    "irsaus",
    "asuaairlt",
    "bzairl",
    "binegij",
    "xcmoei",
    "mmauib",
    "tokoy",
    "caoir",
    "ajnpa",
    "nfcar",
    "segonpari",
    "anir",
    "iedsanino",
    "iaytl",
    "dseewn"
]

num = random.randrange(0, 25, 1)

score = 0
chances = 2


def res():
    global word, answer, num
    num = random.randrange(0, 25, 1)
    lbl.config(text=word[num])
    e1.delete(0, END)


def res1():
    global word, answer, num, score, chances
    num = random.randrange(0, 25, 1)
    lbl.config(text=word[num])
    e1.delete(0, END)
    score = 0
    chances = 2


def default():
    global word, answer, num
    lbl.config(text=word[num])


def checkans():
    global word, answer, num, score, chances
    var = e1.get()
    if var == answer[num]:
        score = score + 1
        lbl2.config(text=('Score', score))
        res()
    else:
        messagebox.showerror("Error", "This is not the correct answer")
        e1.delete(0, END)
        chances = chances - 1
        lbl3.config(text=("Chances", chances))
    if chances == 0:
        messagebox.showwarning("Message", "Game Over")
        messagebox.showinfo("Score is", score)
        res1()
        lbl2.config(text=('Score', score))
        lbl3.config(text=("Chances", chances))

win = tkinter.Tk()
win.geometry("300x400+550+150")
win.title("Jumbled Word Games")
win.configure(background="#000000")

lbl = Label(
    win,
    text=("Jumbled Word"),
    font=("Verdana", 16),
    bg=("#000000"),
    fg=("#ffffff")
)
lbl.pack(pady=20)

lbl2 = Label(
    win,
    text=('Score', score),
    font=("Comic sans ms", 14),
    bg=("#000000"),
    fg=("#ffffff")
)
lbl2.pack()

e1 = Entry(
    win,
    font=("Verdana")
)
e1.pack(pady=20, ipadx=10, ipady=10)

b1 = Button(
    win,
    text=("Check"),
    font=("Caomic sans ms", 12),
    width=14,
    bg=("#4C4B4B"),
    fg=("#6ab04c"),
    relief="raised",
    command=checkans
)
b1.pack(pady=15)

lbl3 = Label(
    win,
    text=("Chances", chances),
    font=("Caomic sans ms", 14),
    bg=("#000000"),
    fg=("#ffffff"),
)
lbl3.pack()
default()

win.mainloop()