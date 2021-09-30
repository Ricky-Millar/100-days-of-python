import random
import time
import paddle, ball, scoreboard, turtle
angle= random.randrange(0,90)
ball = ball.Ball(angle)
timesleep = 0.02
scores = scoreboard.ScoreBoard()
screen = turtle.Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')


player_paddle = paddle.Paddle()
bot_paddle = paddle.Paddle()

player_paddle.player_setup('left')
bot_paddle.bot_setup('right')
screen.tracer(0)
game = True
while game == True:
    scores.score()

    time.sleep(timesleep)
    print(timesleep)

    ball.ball_move()
    screen.update()
    screen.listen()
    screen.onkey(key='s',fun=player_paddle.move_paddle_down)
    screen.onkey(key='w',fun=player_paddle.move_paddle_up)
    screen.onkey(key='Down',fun=bot_paddle.move_paddle_down)
    screen.onkey(key='Up',fun=bot_paddle.move_paddle_up)
    if not -280 < ball.ycor() < 280:
        ball.wall_colision()
        timesleep *= 0.80
    if ball.distance(player_paddle) < 50 and ball.xcor() < -320 or ball.distance(bot_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_colision()
        timesleep *= 0.80
    if ball.xcor() > 400:
        scores.increment_player_score()
        timesleep = 0.02
        ball.goto(0,0)
    if ball.xcor() < -400:
        timesleep = 0.02
        scores.increment_bot_score()
        ball.goto(0, 0)












screen.exitonclick()