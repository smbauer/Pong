from turtle import Turtle
import random

START_HEADINGS = [45, 135, 225, 315]
MOVE_DISTANCE = 20
START_SPEED = 0.1

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # pick a random direction to start the ball moving
        self.setheading(random.choice(START_HEADINGS))
        self.ball_speed = START_SPEED


    def move(self) -> None:
        self.forward(MOVE_DISTANCE)


    def wall_bounce(self) -> None:
        """change direction when the ball hits the walls"""
        current_heading = self.heading()
        new_heading = 360 - current_heading
        self.setheading(new_heading)


    def paddle_bounce(self) -> None:
        """change direction when the ball hits the paddles and increase ball speed"""
        current_heading = self.heading()
        new_heading = 180 - current_heading
        if new_heading < 0:
            new_heading += 360
        self.ball_speed *= 0.9
        self.setheading(new_heading)


    def reset_ball(self) -> None:
        """reset the ball to the center and change direction"""
        self.goto(0, 0)
        self.ball_speed = START_SPEED
        current_heading = self.heading()
        new_heading = 180 - current_heading
        if new_heading < 0:
            new_heading += 360
        self.setheading(new_heading)


    def wall_collision(self) -> bool:
        """returns true when ball hits top or bottom wall"""
        return abs(self.ycor()) >= 280


    def oob_left(self) -> bool:
        """returns true when ball goes oob on left"""
        return self.xcor() <= -480
    

    def oob_right(self) -> bool:
        """returns true when ball goes oob on right"""
        return self.xcor() >= 480


    def paddle_collision(self, paddle) -> bool:
        """returns true when ball makes contact with specified paddle"""
        return abs(self.xcor()) >= 430 and self.distance(paddle) <= 50
    