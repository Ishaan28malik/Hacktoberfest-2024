import sqlite3

class scoring():
	def __init__(self,conn):
		self.your_score = 0
		self.comp_score = 0
		self.con=conn
		self.cur=self.con.cursor()

	def getScore(self, Name):
		try:
			self.cur.execute("Select yscore,cscore from rps where name = '%s'"%(Name))
			score = self.cur.fetchall()
			return(int(score[0][0]), int(score[0][1]))
		except Exception as e:
			self.cur.execute("insert into rps (name, yscore,cscore) values (?,?,?)",(Name,0,0,))
			self.con.commit()
			return (0,0)

	def insertData(self,Name,yscore,cscore):
		self.cur.execute("delete from rps where name = ?", (Name,))
		self.cur.execute("insert into rps (name, yscore, cscore) values (?,?,?)",(Name,yscore,cscore,))
		self.con.commit()