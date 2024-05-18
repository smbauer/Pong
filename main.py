from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# paddle starting positions
R_START = (460, 0)
L_START = (-460, 0)

# create screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# initialize paddles and ball
scoreboard = Scoreboard()
right_paddle = Paddle(pos=R_START)
left_paddle = Paddle(pos=L_START)
ball = Ball()

# set up paddle keystroke mappings
screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="e")
screen.onkeypress(fun=left_paddle.move_down, key="d")
screen.onkey(fun=screen.bye, key="space")
screen.listen()

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.ball_speed)

    # ball bounces off paddle
    if ball.paddle_collision(left_paddle) or ball.paddle_collision(right_paddle):
        ball.paddle_bounce()

    # ball bounces off wall
    if ball.wall_collision():
        ball.wall_bounce()

    # left team scores
    if ball.oob_right():
        scoreboard.point_scored("left")
        ball.reset_ball()

    # right team scores
    if ball.oob_left():
        scoreboard.point_scored("right")
        ball.reset_ball()

    # end condition - either score = 10
    if scoreboard.game_over():
        game_on = False

    ball.move()


screen.exitonclick()
