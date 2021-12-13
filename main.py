from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import Ball
import time
from score_board import ScoreBoard
turtle = Turtle()

# screen setup
screen = Screen()
screen.title("Robpong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# left paddle setup
left_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# right paddle setup
right_paddle = Paddle((350, 0))
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# ball setup
ball = Ball()
ball.move()

# scoreboard setup
scoreboard = ScoreBoard()

# game_is_on
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # wall collision
    if -280 > ball.ycor() or ball.ycor() > 280:
        # ball bounce
        ball.y_bounce()
    # collision with right  and left paddles paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    # out of bounds - right player
    if ball.xcor() > 340:
        scoreboard.r_point()
        ball.reset_position()
    # out of bounds - left player
    if ball.xcor() < -340:
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()