from turtle import Turtle

# PADDLE_SIZE = 3
PADDLE_START_Y = [20, 0, -20]
RIGHT_X = 460
LEFT_X = -460
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle:
    # def __init__(self) -> None:
    #     self.segment = Turtle("square")
    #     self.segment.color("white")
    #     self.segment.penup()
    #     self.segment.goto(x=460, y=0)

    # def move_up(self) -> None:
    #     self.segment.setheading(UP)
    #     self.segment.forward(MOVE_DISTANCE)

    def __init__(self, side) -> None:
        self.segments = []
        self.create_paddle(side)


    def create_paddle(self, side) -> None:
        if side == "right":
            start_x = RIGHT_X
        else:
            start_x = LEFT_X
            
        for y_start in PADDLE_START_Y:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(x=start_x, y=y_start)
            self.segments.append(segment)


    def move_up(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.segments[0].setheading(UP)
        self.segments[0].forward(20)


    def move_down(self) -> None:
        for seg_num in range(len(self.segments) - 1):
            self.segments[seg_num].goto(self.segments[seg_num + 1].pos())
        self.segments[-1].setheading(DOWN)
        self.segments[-1].forward(20)
        # for segment in self.segments():
        #     segment.setheading(UP)
        #     segment.forward(MOVE_DISTANCE)


    # def move_down(self) -> None:
    #     for segment in self.segments():
    #         segment.setheading(DOWN)
    #         segment.forward(MOVE_DISTANCE)