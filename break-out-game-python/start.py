import random
import time
from tkinter import messagebox
from turtle import Screen, tracer
from bounce_panel import BounceBrick
from bricks import Bricks
from ball import Ball


LOWER_LIMIT = 300
UPPER_LIMIT = 250
BALL_START = (0, -200)
COLOR_LIST = ["ffba08", "f48c06", "dc2f02", "6e1423"]

screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("#a4161a")
screen.title("ATARI BREAKOUT")
tracer(0, 0)

brick_x_axis = -LOWER_LIMIT
brick_y_axis = 250
bricks = []
for i in range(7):
    for j in range(10):
        color = random.choice(COLOR_LIST)
        brick = Bricks((brick_x_axis, brick_y_axis), color)
        bricks.append(brick)
        brick_x_axis += 65
    brick_x_axis = -LOWER_LIMIT
    brick_y_axis -= 20

ball = Ball((0, -170))
bounce = BounceBrick(BALL_START)

screen.listen()
screen.onkey(bounce.right, "Right")
screen.onkey(bounce.left, "Left")

is_game_on = True
while is_game_on:
    time.sleep(ball.get_speed())
    screen.update()
    ball.move()

    if ball.ycor() > UPPER_LIMIT:
        ball.bounce_y()

    if ball.xcor() > LOWER_LIMIT+20 or ball.xcor() < -LOWER_LIMIT-20:
        ball.bounce_x()

    if ball.distance(bounce) < 45 and ball.ycor() < 290:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                ball.bounce_x()
            else:
                ball.bounce_x()
                ball.bounce_y()
            bricks.remove(brick)
            break

    if ball.ycor() < -UPPER_LIMIT:
        is_game_on = False
        messagebox.showerror("error", "Oops, the ball went out of bounds")
        if messagebox.OK:
            quit()

    if not bricks:
        is_game_on = False
        messagebox.showinfo("information", "You completed the game, hooray!")
        if messagebox.OK:
            quit()

screen.exitonclick()