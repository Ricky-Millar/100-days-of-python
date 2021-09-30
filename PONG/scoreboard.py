from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,200)
        self.player_score = 0
        self.bot_score = 0
        self.hideturtle()

    def score(self):
        self.write(f"{self.player_score}       {self.bot_score}",False, align="center", font = ("Arial", 70, "bold"))
    def increment_player_score(self):
        self.clear()
        self.player_score += 1
    def increment_bot_score(self):
        self.clear()
        self.bot_score += 1