from turtle import Turtle

HORIZONTAL_LIMIT = 720


class BounceBrick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#161a1d")
        self.shapesize(1, 5)
        self.penup()
        self.goto(position)

    def left(self):
        if self.xcor() > -HORIZONTAL_LIMIT:
            new_x = self.xcor() - 40
            self.goto((new_x, self.ycor()))

    def right(self):
        if self.xcor() < HORIZONTAL_LIMIT:
            new_x = self.xcor() + 40
            self.goto((new_x, self.ycor()))