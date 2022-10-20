from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#4D96FF")
        self.shapesize(stretch_wid=1, stretch_len=15)
        self.penup()
        self.goto(position)
