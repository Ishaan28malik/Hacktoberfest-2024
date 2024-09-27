class Piece():
    def __init__(self, hasBomb):
        self.hasBomb= hasBomb
        self.clicked= False
        self.flagged= False

    def getHasBomb(self):
        return self.hasBomb
    def getClicked(self):
        return self.clicked
    def getFlagged(self):
        return self.flagged

    def setNeighbours(self,neighbours):
        self.neighbours= neighbours   
        self.setNumAround()

    def setNumAround(self):
        self.numAround=0
        for piece in self.neighbours:
            if(piece.getHasBomb()):
                self.numAround+=1

    def getNumAround(self):
        return self.numAround  
    def toggleFlag(self):
        self.flagged= not self.flagged
    def click(self):
        self.clicked=True    
    def getNeighbours(self):
        return self.neighbours