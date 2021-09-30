from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-280,250)


    def write_score(self):
        self.write(f'LEVEL: {self.level}', False, font = FONT, align= 'left')

    def add_score(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER', False, font=FONT, align='center')


