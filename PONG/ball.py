from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self, initial_heading):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed('fastest')
        self.initial_heading = initial_heading
        self.setheading(self.initial_heading)
        self.penup()

    def ball_move(self):
        self.forward(10)


    def wall_colision(self):

        new_heading = 360 - self.heading() + random.randrange(-20, 20)
        self.setheading(new_heading)


    def paddle_colision(self):
        new_heading = 180 - self.heading() + random.randrange(-20, 20)
        self.setheading(new_heading)
