import time
from turtle import Turtle

HEART = '\U0001F49A'


class PointBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('#9CFF2E')
        self.penup()
        self.hideturtle()
        self.score = 0
        try:
            with open('data.txt') as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open('data.txt', 'w') as file:
                file.write('0')
        self.update_point_board()

    def update_point_board(self):
        self.clear()
        self.goto(-350, 370)
        self.write(f'Score: {self.score}\nHigh score: {self.high_score}', align='right', font=('Courier', 23, 'normal'))

    def add_point(self):
        self.score += 1
        self.update_point_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_point_board()


class AttemptsBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('#FF1E00')
        self.penup()
        self.hideturtle()
        self.attempts = 5
        self.update_attempts_board()

    def update_attempts_board(self):
        self.clear()
        self.goto(500, 390)
        self.write(f'{self.attempts * HEART}', align='left', font=('Courier', 25, 'normal'))

    def add_try(self):
        self.attempts -= 1
        self.update_attempts_board()


class EndGame(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def end_game(self):
        self.color('#9CFF2E')
        self.write(f'Ready for the next level!', align='center', font=('Courier', 40, 'normal'))
        time.sleep(3)
        self.reset()
        self.color('#222222')

    def game_over(self):
        self.color('white')
        self.goto(0, 0)
        self.write(f'GAME OVER', align="center", font=("Courier", 50, "bold"))
        self.goto(0, -50)
        self.write(f'press ENTER to continue', align="center", font=("Courier", 30, "bold"))
