from turtle import Screen
from paddle import Paddle


# paddle starting positions
R_START = (460, 0)
L_START = (-460, 0)

# create screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# TODO: set top and bottom of screen as walls
# TODO: set ends as open/oob/nets
# TODO: create a paddle
right_paddle = Paddle(pos=R_START)
left_paddle = Paddle(pos=L_START)

# TODO: move paddle up and down with up/down key presses
screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="e")
screen.onkeypress(fun=left_paddle.move_down, key="d")
screen.onkey(fun=screen.bye, key="space")
screen.listen()

game_on = True

while game_on:
    screen.update()


# TODO: create a second paddle on the opposite side
# TODO: create ball
# TODO: detect angle/direction of ball
# TODO: move ball
# TODO: detect collision with wall
# TODO: detect collision with paddle
# TODO: create scoreboard
# TODO: display each score at top of screen
# TODO: detect when ball goes past the paddles
# TODO: increment score when goal scored
# TODO: draw net

screen.exitonclick()
