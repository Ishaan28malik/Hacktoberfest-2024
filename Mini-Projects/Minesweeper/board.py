from linecache import getlines
from operator import index
from piece import Piece
from random import random
class Board():
    def __init__(self, size,prob):
        self.size= size
        self.prob=prob
        self.lost=False
        self.won= False
        self.numClicked=0
        self.numNonBombs=0
        self.setBoard()

    def setBoard(self):
        self.board=[]
        for row in range(self.size[0]):
            row=[]
            for col in range(self.size[1]):
                hasBomb= random()< self.prob
                if(not hasBomb):
                    self.numNonBombs+=1
                piece =Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbours()    

    def setNeighbours(self) :
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece= self.getPiece((row,col))
                neighbours=self.getListOfNeighbours((row,col))
                piece.setNeighbours(neighbours)

    def getListOfNeighbours(self,index):
        neighbours=[]
        for row in range(index[0]-1,index[0]+2):
            for col in range(index[1]-1,index[1]+2):
                outOfBounds=row<0 or row>=self.size[0] or col<0 or col >=self.size[1]
                same= row ==index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbours.append(self.getPiece((row,col)))
        return neighbours    

    def getSize(self):
        return self.size
    def getPiece(self,index):
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            return
        if(flag):
            piece.toggleFlag() 
            return
        piece.click()  
        if (piece.getHasBomb()):
            self.lost= True  
            return
        self.numClicked+=1   
        if (piece.getNumAround() !=0):
            return
        for neighbour in piece.getNeighbours():
            if( not neighbour.getHasBomb() and not neighbour.getClicked()):
                self.handleClick(neighbour,False)


    def getLost(self):
        return self.lost        
    def getWon(self):
        return self.numNonBombs==self.numClicked
