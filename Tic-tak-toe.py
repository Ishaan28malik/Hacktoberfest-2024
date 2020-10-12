'''
GUI for Tic-tac-toe
using turtle
class verison 
'''
import turtle, random, time

screen = turtle.Screen()
screen.setup(450, 450, 900)
screen.bgcolor("black")
screen.tracer(1)

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #-- Grafic attributes
        self.penup()
        self.hideturtle()
        self.speed(0)
        #-- Game attributes
        self.clear()
        self.y_text_pos = 150
        self.x_text_pos = 60
        self.distance = 80
        self.space = 5
        self.row = 3
        self.col = 3
        self.board = [" "]*9
        self.spot = 0
        self.x = 0
        self.y = 0
        self.count = 0
        self.move = "p"
        self.corners = [0,2,6,8]
        self.win_positions = [[0,1,2],[3,4,5],[6,7,8],
                              [0,3,6],[1,4,7],[2,5,8],
                              [0,4,8],[2,4,6]]

        self.semi_positions = [[0,1,2],[0,2,1],[1,2,0],
                              [3,4,5],[3,5,4],[4,5,3],
                              [6,7,8],[6,8,7],[7,8,6],
                              [0,3,6],[0,6,3],[3,6,0],
                              [1,4,7],[1,7,4],[4,7,1],
                              [2,5,8],[2,8,5],[5,8,2],
                              [0,4,8],[0,8,4],[4,8,0],
                              [2,4,6],[2,6,4],[4,6,2]]
       
    def clear_board(self):
        self.clear()
    def draw_board(self):
        self.pencolor("green")
        self.shape("square")
        self.shapesize(self.distance/20)
        self.fillcolor("black")
        self.setpos(-150, 150)
        #--
        for r in range(self.row):
            for c in range(self.col):
                self.stamp()
                self.forward(self.distance)
            self.back(self.distance * self.row)
            self.right(90)
            self.forward(self.distance)
            self.left(90)

    
    def info(self):
        self.pencolor("yellow")
        self.goto(self.x_text_pos, self.y_text_pos)
        self.write(self.board)
        #self.y_text_pos -= 20

    def check_win(self):
        self.info()
        time.sleep(1)
        self.undo()
        for f,s,t in self.win_positions:
            if self.board[f] == self.board[s] == self.board[t] and self.board[f] != " ":
                return True
    
    def cross(self, x,y):
        self.goto(x-10,y+10)
        self.setheading(-45)
        self.color("white")
        self.pensize(2)
        self.down()
        self.forward(60)
        self.up()
        self.goto(x+30, y+10)
        self.setheading(-135)
        self.down()
        self.forward(60)
        self.up()
        self.hideturtle()

    def get_spot(self, x,y):
        self.spot = None
        if x == -160 and y == 160:
            self.spot = 0
        if x == -80 and y == 160:
            self.spot = 1
        if x == 0 and y == 160:
            self.spot = 2
        if x == -160 and y == 80:
            self.spot = 3
        if x == -80 and y == 80:
            self.spot = 4
        if x == 0 and y == 80:
            self.spot = 5
        if x == -160 and y == 0:
            self.spot = 6
        if x == -80 and y == 0:
            self.spot = 7
        if x == 0 and y == 0:
            self.spot = 8
        return self.spot

    def user(self, x,y):
        try:
            self.move = "x"
            if self.count == 9:
                font = ("arial","14")
                self.goto(-100,-150)
                self.write("Tie", font = font)
                time.sleep(1)
                self.undo()
                main()
            else:
                x = int(self.distance * round(x/self.distance))
                y = int(self.distance * round(y/self.distance))
                self.get_spot(x,y)
                if self.board[self.spot] != " ":
                    font = ("arial","18")
                    self.color("white")
                    self.goto(-100,-150)
                    self.write("Spot is taken", font = font)
                    time.sleep(1)
                    self.undo()
                else:
                    self.board[self.spot] = self.move
                    if self.check_win():
                        self.cross(x,y)
                        font = ("arial","18")
                        self.color("white")
                        self.goto(-100,-150)
                        self.write("You win", font = font)
                        time.sleep(1)
                        self.undo()
                        main()

                    else:
                        self.count += 1
                        self.cross(x,y)
                        self.computer()
        except TypeError:
            font = ("arial","18")
            self.color("white")
            self.goto(-100,-150)
            self.write("Click on board", font = font)
            time.sleep(1)
            self.undo()
            

    def computer(self):
        self.move = "o"
        if self.count == 9:
            font = ("arial","18")
            self.color("white")
            self.goto(-100,-150)
            self.write("Tie", font = font)
            time.sleep(1)
            self.undo()
            main()
        else:
            c_spot = self.get_opening()
            if c_spot == None:

                for f,s,t in self.semi_positions:
                    if self.board[f] == "o" and self.board[s] == "o":
                        if self.board[t] == " ":
                            c_spot = t

            if c_spot == None:
                for f,s,t in self.semi_positions:
                    if self.board[f] == "x" and self.board[s] == "x":
                        if self.board[t] == " ":
                            c_spot = t
            if c_spot == None:
                font = ("arial","18")
                self.color("white")
                self.goto(-100,-150)
                self.write("Thinking", font = font)
                time.sleep(1)
                self.undo()
                c_spot = random.randrange(0,9)
                self.goto(-100,-150)
                self.write(c_spot, font = font)
                time.sleep(1)
                self.undo()
                while self.board[c_spot] != " ":
                    c_spot = random.randrange(0,9)
                    if self.board[c_spot] ==" ":
                        break

            if c_spot == 0:
                self.x = -160
                self.y = 160
            if c_spot == 1:
                self.x = -80
                self.y = 160
            if c_spot == 2:
                self.x = 0
                self.y = 160
            if c_spot == 3:
                self.x = -160
                self.y = 80
            if c_spot == 4:
                self.x = -80
                self.y = 80
            if c_spot == 5:
                self.x = 0
                self.y = 80
            if c_spot == 6:
                self.x = -160
                self.y = 0
            if c_spot == 7:
                self.x = -80
                self.y = 0
            if c_spot == 8:
                self.x = 0
                self.y = 0
                
            self.shape("circle")
            self.shapesize(2.5)
            self.pencolor("red")
            self.pensize(2)
            self.fillcolor("black")
            self.goto(self.x+10,self.y-10)
            self.board[c_spot] = self.move
            self.count += 1        
            self.stamp()
            self.info()
            time.sleep(1)
            self.undo()
            for f,s,t in self.win_positions:
                if self.board[f] == self.board[s] == self.board[t] and self.board[f] != " ":
                   font = ("arial","14")
                   self.color("white")
                   self.goto(-100,-150)
                   self.write("I win", font = font)
                   time.sleep(1)
                   self.undo()
                   main()
            if self.count == 9:
                font = ("arial","18")
                self.goto(-100,-150)
                self.color("white")
                self.write("Tie", font = font)
                time.sleep(1)
                self.undo()
                main()
                             
    def get_opening(self):
       if self.count == 0:
           c_spot = random.choice(self.corners)
           return c_spot
       if self.count == 1:
           if self.board[4] == " ":
               c_spot = 4
               return c_spot
           if self.count != " ":
               c_spot = random.choice(self.corners)
               return c_spot

def main():
    game = Game()
    game.clear_board()
    turn = random.randrange(0,2)
    if  turn == 0:
        game = Game()
        game.clear_board()
        game.draw_board()
        font = ("arial","18")
        game.goto(-100,-150)
        game.color("white")
        game.write("Your turn, play", font = font)
        time.sleep(1)
        game.undo()
        turtle.onscreenclick(game.user)
    else:
        game = Game()
        game.clear_board()
        game.draw_board()
        font = ("arial","18")
        game.goto(-100,-150)
        game.color("white")
        game.write("My turn wait!", font = font)
        time.sleep(1)
        game.undo()
        turtle.onscreenclick(game.user)
        game.computer()
    print(turn)
    
if __name__ =="__main__":
    main()

turtle.mainloop()
