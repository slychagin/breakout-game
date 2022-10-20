from turtle import Turtle

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900


class Blocks(Turtle):
    """
    Create blocks, set block color
    """

    def __init__(self):
        super().__init__()
        self.color('#222222')
        self.all_blocks = []

    def create_block(self, rows, y_delta=20):
        for row in range(1, rows):
            for block in range(1, 14):
                new_block = Turtle('square')
                new_block.shapesize(stretch_wid=2, stretch_len=5)
                if row in [1, 2]:
                    new_block.color('#7DCE13')
                if row in [3, 4]:
                    new_block.color('#FCE700')
                if row in [5, 6]:
                    new_block.color('#FF884B')
                if row in [7, 8]:
                    new_block.color('#CC3636')
                if row > 8:
                    new_block.color('#790252')

                new_block.penup()

                if block <= 6:
                    x_cor = - (SCREEN_WIDTH/2 - block * 106 + 45)
                    y_cor = 45 * row - y_delta
                else:
                    x_cor = SCREEN_WIDTH - block * 106 - 25
                    y_cor = 45 * row - y_delta

                new_block.goto(x_cor, y_cor)
                self.all_blocks.append(new_block)


class Bang(Turtle):
    """
    Show bang after collisions
    """

    def __init__(self):
        super().__init__()
        self.screen.addshape('bang.gif')
        self.shape('bang.gif')
        self.penup()
        self.hideturtle()

    def move_bang(self, x, y):
        self.goto(x, y)
        self.showturtle()
