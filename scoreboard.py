FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write(f" GAME OVER!!!", align="center", font=FONT)
