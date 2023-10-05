from tkinter import *
import sqlite3

class showDatabase:
	def __init__(self, conn, root, home):
		self.con=conn
		self.cur=self.con.cursor()
		self.root = root
		self.gameScreen = home
		self.root.title("Scoreboard")
		self.root.configure(height=675,width=675)
		self.root.config(background='white')
		self.root.resizable(0,0)
		self.back = PhotoImage(file = 'icons/back.png')
		self.delete = PhotoImage(file = 'icons/delete.png')
		self.nameLabel = Label(self.root,text= "Name".center(23),bg="SpringGreen2",fg='black',font='Arial 20 bold')
		self.yscoreLabel = Label(self.root,text="Your Score".center(20).center(20),bg="SpringGreen2",fg='black',font='Arial 20 bold')
		self.cscoreLabel = Label(self.root,text= "Computer Score".center(20) ,bg="SpringGreen2",fg='black',font='Arial 20 bold')
		self.resetButton = Button(self.root, text="Reset", bg="khaki1", fg="brown", command= lambda : self.delete(home))
		self.backButton = Button(self.root, image=self.back, bg="white", borderwidth=0,highlightthickness = 0, command= lambda :self.deleteWindow(home))
		self.deleteLabel = Label(self.root,text= "".center(5) ,bg="SpringGreen2",fg='black',font='Arial 20 bold')
		self.tableSize = 22
		self.labelList = []
		for i in range(1,self.tableSize):
			if i%2==0:
				color = "plum1"
			else:
				color = "PaleTurquoise1"
			self.labelList.append([Label(self.root, text="".center(25), bg=color),Label(self.root, text="".center(20), bg=color),Label(self.root, text="".center(20), bg=color), Label(self.root, bg=color)])

	def createWindow(self):
		## CREATING LABELS FOR COLUMN HEADER
		self.nameLabel.grid(row=0,column=1, sticky='ew')
		self.yscoreLabel.grid(row=0,column=2, sticky='ew')
		self.cscoreLabel.grid(row=0,column=3, sticky='ew')
		self.resetButton.grid(row=self.tableSize+1,column=2, sticky='e')
		self.backButton.grid(row=self.tableSize+1,column=2, sticky='w')
		self.deleteLabel.grid(row=0,column=4, sticky='ew')

	def score(self):
		try:
			self.cur.execute("create table if not exists rps(name varchar2(10),yscore varchar2(5),cscore varchar2(5))")
		except Exception as e:
			pass

		self.createWindow()
		## SELECTING ROWS BY DECREASING ORDER OF COMPUTER SCORE
		self.cur.execute('select * from rps order by cscore DESC')
		rows=self.cur.fetchall()
		# FETCHING EACH ROW
		for i in range(1,self.tableSize):
			if i%2==0:
				color = "plum1"
			else:
				color = "PaleTurquoise1"
			if i <= len(rows):
				name,yscore,cscore = rows[i-1][0],rows[i-1][1],rows[i-1][2]
				self.labelList[i-1][3].configure(image=self.delete)
				self.labelList[i-1][3].bind('<Button-1>', lambda event, arg=name:self.deleteEntry(event,arg))
			else:
				self.labelList[i-1][3].configure(text= "".center(5) ,bg=color,fg='black',font='Arial 15 bold')
				name,yscore,cscore = "", "", ""
			self.labelList[i-1][0].configure(text = str(name).center(25),bg=color,fg='black',font='Arial 15')
			self.labelList[i-1][1].configure(text = str(yscore).center(20),bg=color,fg='black',font='Arial 15')
			self.labelList[i-1][2].configure(text = str(cscore).center(20),bg=color,fg='black',font='Arial 15')
			self.labelList[i-1][0].grid(row = i, column=1,sticky='ew')
			self.labelList[i-1][1].grid(row = i, column=2,sticky='ew')
			self.labelList[i-1][2].grid(row = i, column=3,sticky='ew')
			self.labelList[i-1][3].grid(row = i, column=4,sticky='ew')
		self.root.update()
		self.root.mainloop()

	def delete(self, home):
		self.cur.execute("drop table rps")
		self.con.commit()
		self.score()

	def deleteEntry(self,event,name):
		print("Deleted " + str(name))
		self.cur.execute("delete from rps where name = ?",(name,))
		self.con.commit()
		self.nameLabel.grid_forget()
		self.yscoreLabel.grid_forget()
		self.cscoreLabel.grid_forget()
		self.resetButton.grid_forget()
		self.backButton.grid_forget()
		self.deleteLabel.grid_forget()
		for i in range(1,self.tableSize):
			self.labelList[i-1][0].grid_forget()
			self.labelList[i-1][1].grid_forget()
			self.labelList[i-1][2].grid_forget()
			self.labelList[i-1][3].grid_forget()
		self.__init__(self.con, self.root, self.gameScreen)
		self.score()


	def deleteWindow(self, home):
		self.nameLabel.grid_forget()
		self.yscoreLabel.grid_forget()
		self.cscoreLabel.grid_forget()
		self.resetButton.grid_forget()
		self.backButton.grid_forget()
		self.deleteLabel.grid_forget()
		for i in range(1,self.tableSize):
			self.labelList[i-1][0].grid_forget()
			self.labelList[i-1][1].grid_forget()
			self.labelList[i-1][2].grid_forget()
			self.labelList[i-1][3].grid_forget()
		home()
