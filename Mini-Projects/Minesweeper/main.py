from game import Game
from board import Board
size=(9,9)
prob=0.15
board=Board(size,prob)
screenSize=(460,460) #width,height
game=Game(board,screenSize)
game.run()





