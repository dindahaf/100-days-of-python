from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(start_position)

    def up(self):
        current_y = self.ycor()
        self.sety(current_y + 100)

    def down(self):
        current_y = self.ycor()
        self.sety(current_y - 100)