import random
import turtle
import math
from turtle import Turtle


class HerstPainter:


    def __init__(self):
        self.width = 10
        self.colour_list = [(150, 150, 150)]
        turtle.colormode(255)
        turtle.penup()


    def draw_dot_painting(self, width, colour_list, dot_size, gap_size):
        canvas = turtle.Screen()


        self.dot_size = dot_size
        self.gap_size = gap_size
        self.width = width
        self.colour_list = colour_list
        canvas.bgcolor(colour_list[0])
        turtle.setheading(0)
        turtle.setpos(-int(width*(dot_size) / 2), -int(width*(dot_size) / 2))
        turtle.speed('fastest')
        for i in range(int(width/2)):
            for i in range(width):
                turtle.dot(self.gap_size, random.choice(self.colour_list))
                turtle.forward(self.dot_size)
            turtle.dot(self.gap_size, random.choice(self.colour_list))
            turtle.setheading(90)
            turtle.forward(self.dot_size)
            turtle.setheading(180)
            for i in range(width):
                turtle.dot(self.gap_size, random.choice(self.colour_list))
                turtle.forward(self.dot_size)
            turtle.dot(self.gap_size, random.choice(self.colour_list))
            turtle.setheading(90)
            turtle.forward(self.dot_size)
            turtle.setheading(0)
        turtle.exitonclick()



    def draw_ordered_painting(self, colour_list, dot_size, gap_size):
        canvas = turtle.Screen()
        self.dot_size = dot_size
        self.gap_size = gap_size
        length = int(math.sqrt(len(colour_list)))
        self.colour_list = colour_list
        turtle.setheading(0)
        turtle.setpos(-int(length * (dot_size) / 2), -int(length * (dot_size) / 2))
        turtle.speed('fastest')
        for i in range(int(length / 2)):
            for i in range(length):
                turtle.dot(self.gap_size, random.choice(self.colour_list))
                turtle.forward(self.dot_size)
            turtle.dot(self.gap_size, random.choice(self.colour_list))
            turtle.setheading(90)
            turtle.forward(self.dot_size)
            turtle.setheading(180)
            for i in range(length):
                turtle.dot(self.gap_size, random.choice(self.colour_list))
                turtle.forward(self.dot_size)
            turtle.dot(self.gap_size, random.choice(self.colour_list))
            turtle.setheading(90)
            turtle.forward(self.dot_size)
            turtle.setheading(0)
        turtle.exitonclick()