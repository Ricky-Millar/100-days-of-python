from flask import Flask
import random
app = Flask(__name__)
num = 0

def new_num():
    global num
    num = random.randrange(0,9)
new_num()
@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<img src="https://c.tenor.com/lIy9f2NtVZMAAAAC/count-down-movie-countdown.gif">'

@app.route('/<int:guess>')
def random_num(guess):
    global num
    if guess == num:
        new_num()
        return "WOOP"
    if guess > num:
        return "too high"
    if guess < num:
        return "too low"


if __name__ == '__main__':
    #this restarts the server when new code is saved and also opens up other debug tools
    app.run(debug=True)