from turtle import Turtle

PADDLE_SIZE = 5
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, pos) -> None:
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=PADDLE_SIZE, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(pos)
        self.setheading(UP)


    def move_up(self) -> None:
        """move the paddle upwards"""
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)


    def move_down(self) -> None:
        """move the paddle downwards"""
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)