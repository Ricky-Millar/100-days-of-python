import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
from random import Random
anglist = [90, 270, 0, 180]
def random_colour():
    R = random.randint(1,255)
    G = random.randint(1,255)
    B = random.randint(1,255)
    colourtupple = (R, G, B)
    return colourtupple

timmy = Turtle()
timmy.pensize(2)
screen = Screen()
timmy.shape('turtle')
timmy.speed(0)

def draw_spyrograph(turns, size):
    for i in range(turns):
        timmy.color(random_colour())
        timmy.circle(size)
        timmy.right(360/turns)



draw_spyrograph(int(input("how many turns?")),int(input("how big")))
screen.exitonclick()