import time
from turtle import Turtle

START_POSITION = (0, -410)


class Ball(Turtle):
    """
    Create ball, set ball speed and rebounds
    """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('#B2B2B2')
        self.penup()
        self.goto(START_POSITION)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.02

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebound_y(self):
        self.y_move *= -1

    def rebound_x(self):
        self.x_move *= -1

    def reset_screen(self):
        time.sleep(1)
        self.goto(0, -360)
        self.rebound_y()

    def speed_up(self):
        self.move_speed *= 0.9

    def stop(self):
        self.goto(START_POSITION)
        self.x_move = 0
        self.y_move = 0
