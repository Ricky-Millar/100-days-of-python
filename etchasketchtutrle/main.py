import turtle
import matplotlib.pyplot as plt
import random
board = turtle.Screen()
board.colormode(255)

width = 500
height = 400
startpos = []
turtleholder = {}
board.setup(width = width,height = height)
height *= 0.9
numofturtles = int(turtle.textinput('who','how many turtles?'))
def randomcolor():
    color = []
    for i in range(3):
        color.append(random.randrange(0,255))
    return color

def create_start_pos(numofturtles):
    spacing = height / numofturtles+2
    x = int((-width)/2)
    base = (-height/2)
    for i in range(numofturtles):
        y =  int(base + spacing*i)
        startpos.append([x,y])
    for i in range(numofturtles):
        color = randomcolor()
        turtleholder['competitor' + str(i)] = turtle.Turtle()
        turtleholder['competitor' + str(i)].shape('turtle')
        turtleholder['competitor' + str(i)].color(color)
        turtleholder['competitor' + str(i)].penup()
        turtleholder['competitor' + str(i)].setpos(startpos[i][0],startpos[i][1])
        turtleholder['competitor' + str(i)].pendown()
        turtleholder['competitor' + str(i)].setheading(0)




print(create_start_pos(numofturtles))
winner = 0
game = True
user_bet = turtle.textinput('take your betss','WHOOO GUN WIN?')
def progress_race():
    global game , winner
    for i in range(numofturtles):

        turtleholder['competitor' + str(i)].forward(random.randrange(0,20))
        if turtleholder['competitor' + str(i)].xcor() >= int((width/2)-20):
            game = False
            winner = i
            return

while game == True:
    progress_race()
    WinningTurtle = winner+1

if int(user_bet) == WinningTurtle:
    print(f'Turtle number {WinningTurtle} won! Congratz')
else:
    turtleholder['competitor' + str(winner)].write("you lose", True, align="left")


board.exitonclick()