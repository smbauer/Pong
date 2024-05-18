from turtle import Turtle
import time


SCOREBOARD_LOCATION = (0, 250)
ALIGNMENT = "center"
FONT = ("Courier", 36, "normal")
WIN_SCORE = 5


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.left_score = 0
        self.right_score = 0
        self.refresh_scoreboard()


    def refresh_scoreboard(self) -> None:
        """update the scoreboard with the current score at the top of the screen"""
        self.clear()
        self.goto(SCOREBOARD_LOCATION)
        self.write(f"{self.left_score} : {self.right_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self, team) -> None:
        """increment the current score"""
        if team == "left":
            self.left_score += 1
        elif team == "right":
            self.right_score += 1
        self.refresh_scoreboard()


    def point_scored(self, team) -> None:
        """write point scored message in the middle of the screen"""
        self.clear()
        self.goto(0, 0)
        self.write(f"Point Scored: {team.capitalize()}", align=ALIGNMENT, font=FONT)
        time.sleep(2)
        self.increase_score(team)


    def game_over(self) -> bool:
        """
        returns true if either team has won and prints the game over message.
        otherwise returns false.
        """
        if self.left_score < WIN_SCORE and self.right_score < WIN_SCORE:
            return False
        elif self.left_score == WIN_SCORE:
            winner = "Left"
        elif self.right_score == WIN_SCORE:
            winner = "Right"
        
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over: {winner} Team Wins {self.left_score}-{self.right_score} ",
                    align=ALIGNMENT, font=FONT)
        
        return True
