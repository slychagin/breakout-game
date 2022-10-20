import os
import sys
import time
from turtle import Screen
from ball import Ball
from blocks import Blocks, Bang
from board import PointBoard, AttemptsBoard, EndGame
from paddle import Paddle

Y_DELTA = 20
ROWS_NUMBER = 9

# CREATE SCREEN
screen = Screen()
screen.bgcolor('#222222')
screen.title('Breakout Game')
screen.setup(width=1400, height=900)
screen.tracer(0)

# CREATE OBJECTS
paddle = Paddle((0, -430))
ball = Ball()
blocks_creator = Blocks()
blocks_creator.create_block(ROWS_NUMBER)
bang = Bang()
points = PointBoard()
attempt = AttemptsBoard()
endgame = EndGame()


# BIND PADDLE WITH MOUSE CURSOR
def on_move(self, fun, add=None):
    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun((self.cv.canvasx(event.x) / self.xscale), -430)

        self.cv.bind('<Motion>', eventfun, add)


def goto_handler(x, y):
    on_move(paddle.screen, None)
    paddle.setheading(paddle.towards(x, y))
    paddle.goto(x, y)
    on_move(paddle.screen, goto_handler)


on_move(paddle.screen, goto_handler)


# RESTART GAME
def restart():
    refresh = sys.executable
    os.execl(refresh, refresh, *sys.argv)


screen.listen()
screen.onkeypress(restart, 'Return')


# START GAME
while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # COLLISIONS
    if ball.xcor() > 680 or ball.xcor() < -680:
        ball.rebound_x()

    if ball.ycor() > 430:
        ball.rebound_y()

    if ball.distance(paddle) < 150 and ball.ycor() < -410:
        ball.rebound_y()

    if ball.ycor() < -460:
        attempt.add_try()
        ball.reset_screen()

    # COLLISIONS WITH BLOCKS
    for block in blocks_creator.all_blocks:
        if ball.distance(block) < 50:
            x_cor = block.xcor()
            y_cor = block.ycor()

            blocks_creator.all_blocks.remove(block)
            block.hideturtle()

            ball.rebound_y()
            bang.move_bang(x_cor, y_cor)
            points.add_point()
            ball.speed_up()

    # END GAME
    if attempt.attempts < 0:
        points.reset()
        endgame.game_over()
        break

    if len(blocks_creator.all_blocks) == 0:
        ball.stop()
        endgame.end_game()
        points.reset()

        ROWS_NUMBER += 1
        Y_DELTA += 45
        blocks_creator.create_block(ROWS_NUMBER, Y_DELTA)
        ball.x_move = 10
        ball.y_move = 10
        ball.move()

screen.exitonclick()
