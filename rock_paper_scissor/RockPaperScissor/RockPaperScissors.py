from tkinter import *
from tkinter import messagebox
import random
import sqlite3
import os
import sys
sys.path.append('./lib/')
from database import showDatabase
from game import playGame

class rockPaperScissors:
	def __init__(self):
		self.con=sqlite3.Connection('scoreboard.db')
		self.cur=self.con.cursor()
		self.root=Tk()
		self.title = Label(self.root,text='Rock Paper Scissor',relief='ridge',font='times 40 bold',fg='midnight blue', bg="white",borderwidth=0,highlightthickness = 0)
		self.logo = PhotoImage(file='icons/logo.png')
		self.logo_image = Label(self.root,image=self.logo, bg="white")
		self.versionLabel = Label(self.root,text='( Ver 1.0 )',font='times 13 italic',bg='white', fg="VioletRed1")
		self.nameLabel = Label(self.root,text='Enter Your Name Please :',font='times 20 bold',bg='white', fg="VioletRed3")
		self.nameEntry = Entry(self.root,font='times 15 bold',bg='ivory',fg = "dark orange", width = 40)
		self.submitButton = None
		self.openSourceLabel = None
		self.scoreboardButton = None

	def play(self,userName):
		self.cur.execute("create table if not exists rps(name varchar2(10),yscore varchar2(5),cscore varchar2(5))")
		self.con.commit()
		self.wipe()
		gameObject = playGame(userName, self.con, self.root)
		temp_scores= gameObject.myGame(self.game)

	def fun(self):
		if self.nameEntry.get()=='':
			messagebox.showerror('missing input','please fill Name')
		else:
			temp_scores = self.play(self.nameEntry.get())

	def score(self):
		db = showDatabase(self.con,self.root, self.game)
		self.wipe()
		db.score()
		self.con.commit()

	def createHomeWinodw(self):
		self.title.place(x=110,y=320)
		self.logo_image.place(x=180,y=0)
		self.versionLabel.place(x=330,y=390, anchor=CENTER)
		self.nameLabel.place(x=80,y=430, anchor=CENTER)
		self.nameEntry.place(x=5,y=450, width=650,height=30)
		self.openSourceLabel.place(x=210,y=620)
		self.scoreboardButton.place(x=275,y=550)
		self.submitButton.place(x=287,y=500)

	def wipe(self):
		self.title.place_forget()
		self.logo_image.place_forget()
		self.versionLabel.place_forget()
		self.nameLabel.place_forget()
		self.nameEntry.place_forget()
		self.submitButton.place_forget()
		self.scoreboardButton.place_forget()
		self.openSourceLabel.place_forget()
		self.root.update()

	def game(self):
		self.submitButton = Button(self.root,text="SUBMIT",bg='misty rose',fg="blue4",height='1',width='6',command=self.fun)
		self.openSourceLabel = Label(self.root,text='Made With '+ u"\u2764" + ' of Open Source',relief='ridge',font='times 13 bold',fg='red', bg="white",borderwidth=0,highlightthickness = 0)
		self.scoreboardButton = Button(self.root,text='Scoreboard',bg='tomato',fg = "blue4",height='1',width='9',command=self.score)
		self.createHomeWinodw()
		## Changed Background
		self.root.configure(bg="white")

		## locks the window so that It does not look vague on expandng
		self.root.resizable(0,0)
		self.root.configure(height=675,width=675)
		self.root.title("Rock Paper Scissors")
		self.root.mainloop()

g = rockPaperScissors()
g.game()