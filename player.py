from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        # self.shape("square")
        # self.turtlesize(stretch_wid=2, stretch_len=1, outline=None)
        self.y_pos = -280
        self.penup()
        self.left(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.y_pos += MOVE_DISTANCE
        self.goto(self.xcor(), self.y_pos)

    def restart_turtle(self):
        self.goto(STARTING_POSITION)

    def success_cross(self):
        if self.ycor() > 280:
            print("is at finish line!!!")
            self.y_pos = -280
            self.goto(STARTING_POSITION)
            return True
        else:
            return False
