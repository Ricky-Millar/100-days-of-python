from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid = 5, stretch_len= 1)
        self.penup()
        self.speed('fastest')

    def bot_setup(self, side):
        if side == 'left':
            self.setpos(y=0,x=-350)
        if side == 'right':
            self.setpos(y=0, x=350)

    def player_setup(self, side):
        if side == 'left':
            self.setpos(y=0,x=-350)
        if side == 'right':
            self.setpos(y=0, x=350)


    def move_paddle_up(self):
        if self.ycor() < 250:
            newycor = self.ycor() + 50
            self.goto(self.xcor(),newycor)

    def move_paddle_down(self):
        if -250 < self.ycor():
            newycor = self.ycor() - 50
            self.goto(self.xcor(), newycor)



