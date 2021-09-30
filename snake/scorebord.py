from turtle import Turtle


class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.penup
        self.score = 0
        with open('highscores.txt', mode = 'r') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.hideturtle()
        self.goto(0, 280)
        self.clear()
        self.write(f'Your score is: {self.score}, Highscore: {self.highscore}', False, align='center')

    def add_score(self):
        self.clear()
        self.score += 1
        if self.score > self.highscore:
            with open('highscores.txt', mode='w') as file:
                file.write(str(self.score))
            self.highscore = self.score

        self.write(f'Your score is: {self.score}, Highscore: {self.highscore}', False, align='center')

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.color('black')
        self.write(f"OH NOOOO!\n Final score: {self.score}", False, align='center', font=("Arial", 30, "normal"))
