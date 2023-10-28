from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("#ffffff")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.05
        self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def get_speed(self):
        return self.speed