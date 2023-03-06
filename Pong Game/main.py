from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

r_score = 0
l_score = 0
game_on = True
while game_on:
    # time.sleep(0.001)
    # screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball goes out of bounds.

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_score_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_score_r()




screen.exitonclick()
