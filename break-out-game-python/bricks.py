from turtle import Turtle


class Bricks(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.color(f"#{color}")
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=0.75)
        self.penup()
        self.goto(position)