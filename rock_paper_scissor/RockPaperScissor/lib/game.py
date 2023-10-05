from tkinter import *
import time
import random
from updateScore import scoring

class playGame:

	def __init__(self, userName, conn, root):
		self.root = root
		self.user_name = userName
		self.scoreboard = scoring(conn)
		self.user_score, self.comp_score = self.scoreboard.getScore(userName)
		self.logo=PhotoImage(file='icons/logo.png')
		self.iconRock = PhotoImage(file='icons/iconRock.png')
		self.iconPaper = PhotoImage(file='icons/iconPaper.png')
		self.iconScissors = PhotoImage(file='icons/iconScissors.png')
		self.outputRock = PhotoImage(file='icons/outputRock.png')
		self.outputPaper = PhotoImage(file='icons/outputPaper.png')
		self.outputScissors = PhotoImage(file='icons/outputScissors.png')
		self.user = PhotoImage(file='icons/user.png')
		self.computer = PhotoImage(file='icons/computer.png')
		self.root.title("Let's Play !!")
		self.root.configure(bg="white")
		self.titleLabel = Label(self.root,text='Hello '+self.user_name+' Hit Your Choice!!',font='times 20 bold',bg='white',fg="SlateBlue2",width=52,height=1,anchor=CENTER)
		self.userScoreLabel  = Label(self.root,text='User Score: %d'%(self.user_score),font='times 20 bold',bg='white',fg="red",anchor=CENTER,width=24,height=1)
		self.compScoreLabel = Label(self.root,text='Computer Score: %d'%(self.comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1)
		self.resultTextLabel = Label(self.root,text='~ Result ~',font='times 20 bold',bg='pink',fg="midnight blue",anchor=CENTER,width=52,height=1)
		self.chooseLabel = Label(self.root,text='~ Choose ~',font='times 20 bold',bg='pink',fg="midnight blue",anchor=CENTER,width=52,height=1)
		self.userImage = Label(self.root,image=self.user,bg="white",height=300,width=250)
		self.compImage = Label(self.root,image=self.computer,bg="white",height=300,width=250)
		self.resultLabel = Label(self.root,text='',font='times 15 bold',bg="white",fg="green",width=67,height=1,anchor=CENTER)
		self.rockButton = Button(self.root, image = self.iconRock,bg='white',height=50,width=50,borderwidth=0,highlightthickness = 0)
		self.paperButton = Button(self.root, image = self.iconPaper,bg='white',height=50,width=50,borderwidth=0,highlightthickness = 0)
		self.scissorButton = Button(self.root, image = self.iconScissors,bg='white',height=53,width=50,borderwidth=0,highlightthickness = 0)
		self.openSourceLabel = Label(self.root,text='Made With '+ u"\u2764" + ' of Open Source',relief='ridge',font='times 13 bold',fg='red', bg="white",borderwidth=0,highlightthickness = 0, height=1, width=75, anchor=CENTER)
		self.back = PhotoImage(file = 'icons/back.png')
		self.backButton = Button(self.root, image = self.back, bg="white", borderwidth=0,highlightthickness = 0)

	def Rock(self):
		comp = random.randint(1,3)
		if comp == 3:
			self.user_score+=1
			for i in range(5):
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputRock)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputPaper)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputScissors)
			self.userScoreLabel.configure(text='User Score: %d'%(self.user_score))
			self.resultLabel.configure(text='YOU WON, Keep It Coming !!', fg="green")
		elif comp==1: 
			for i in range(5):
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputScissors)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputPaper)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputRock)
			self.resultLabel.configure(text="It's a TIE",fg="saddle brown")
		else:
			self.comp_score+=1
			for i in range(5):
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputRock)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputScissors)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputPaper)
			self.compScoreLabel.configure(text='Computer Score: %d'%(self.comp_score))
			self.resultLabel.configure(text='YOU LOST, Try Again', fg="red")
		# 
	def paper(self):
		comp = random.randint(1,3)
		if comp == 1:
			self.user_score+=1
			for i in range(5):
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputScissors)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputPaper)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputRock)
			self.userScoreLabel.configure(text='User Score: %d'%(self.user_score))
			self.resultLabel.configure(text='YOU WON, Keep It Coming !!', fg="green")
		elif comp==2:
			for i in range(5):
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputRock)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputScissors)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputPaper)
			self.resultLabel.configure(text="It's a TIE",fg="saddle brown")
		else:
			self.comp_score+=1
			for i in range(5):
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputRock)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputPaper)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputScissors)
			self.compScoreLabel.configure(text='Computer Score: %d'%(self.comp_score))
			self.resultLabel.configure(text='YOU LOST, Try Again', fg="red")	
			
	def scissor(self):
		comp = random.randint(1,3)
		if comp == 2:
			self.user_score+=1
			for i in range(5):
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputRock)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputScissors)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputPaper)
			self.userScoreLabel.configure(text='User Score: %d'%(self.user_score))
			self.resultLabel.configure(text='YOU WON, Keep It Coming !!', fg="green")
		elif comp==3:
			for i in range(5):
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputRock)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputPaper)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputScissors)
			self.resultLabel.configure(text="It's a TIE",fg="saddle brown")
		
		else:
			self.comp_score+=1
			for i in range(5):
				self.userImage.configure(image=self.outputPaper)
				self.compImage.configure(image=self.outputScissors)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputRock)
				self.compImage.configure(image=self.outputPaper)
				self.root.update()
				time.sleep(.1)
				self.userImage.configure(image=self.outputScissors)
				self.compImage.configure(image=self.outputRock)
			self.compScoreLabel.configure(text='Computer Score: %d'%(self.comp_score))
			self.resultLabel.configure(text='YOU LOST, Try Again', fg="red")
	
	def destroyWindow(self):
		self.titleLabel.place_forget()
		self.backButton.place_forget()
		self.userScoreLabel.place_forget()
		self.compScoreLabel.place_forget()
		self.resultTextLabel.place_forget()
		self.chooseLabel.place_forget()
		self.userImage.place_forget()
		self.compImage.place_forget()
		self.resultLabel.place_forget()
		self.rockButton.place_forget()
		self.paperButton.place_forget()
		self.scissorButton.place_forget()
		self.openSourceLabel.place_forget()

	def onBackToHome(self, game):
		self.scoreboard.insertData(self.user_name,self.user_score, self.comp_score)
		# print(self.user_name,self.user_score, self.comp_score)
		self.destroyWindow()
		self.root.update()
		game()

	def createWindow(self, game):
		self.titleLabel.place(x=0, y=10)
		self.userScoreLabel.place(x=0, y=65)
		self.compScoreLabel.place(x=340, y=65)
		self.resultTextLabel.place(x=0, y=520)
		self.chooseLabel.place(x=0, y=410)
		self.userImage.place(x=30,y=100)
		self.compImage.place(x=400,y=100)
		self.resultLabel.place(x=0, y=560)
		self.rockButton.configure(command=self.Rock)
		self.paperButton.configure(command=self.paper)
		self.scissorButton.configure(command=self.scissor)
		self.backButton.configure(command = lambda:self.onBackToHome(game))
		self.backButton.place(x=0,y=0)
		self.rockButton.place(x=240,y=450)
		self.paperButton.place(x=310,y=450)
		self.scissorButton.place(x=380,y=447)
		self.openSourceLabel.place(x=0,y=635)
	
	def myGame(self, game):
		self.createWindow(game)
		self.root.resizable(0,0)
		self.root.geometry('675x675')
		self.root.mainloop()
		return (self.user_score,self.comp_score)