#-------------------------- SETUP ------------------------------- #
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
TITLEFONT = ('Ariel', 40 , 'italic')
WORDFONT = ('Ariel', 60 , 'bold')
words = {}
try:
    data_frame = pandas.read_csv('data/words_to_learn.csv')
except:
    data_frame = pandas.read_csv('data/french_words.csv')
to_learn = data_frame.to_dict(orient = 'records')
print(to_learn)

#-------------------------- Inner Workings ------------------------------- #
def save_data():
    global words, to_learn
    to_learn.remove(words)
    data_frame = pandas.DataFrame.from_dict(to_learn, orient='columns')
    data_frame.to_csv('data/words_to_learn.csv', index = False)
    if len(to_learn) == 0:
        data_frame = pandas.read_csv('data/french_words.csv')
        to_learn = data_frame.to_dict(orient='records')
def flip_card():
    global words
    canvas.itemconfig(card, image=BgCard)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=words['English'], fill='white')
    canvas.itemconfig(card_Counter, text=f'Remaining Cards: {len(to_learn)}', fill='white')
    canvas.update()

def reset_card():
    global words
    canvas.itemconfig(card, image=FgCard)
    canvas.itemconfig(card_title, text = 'French',fill='black')
    canvas.itemconfig(card_word, text=words['French'],fill='black')
    canvas.itemconfig(card_Counter, text=f'Remaining Cards: {len(to_learn)}', fill='black')
    canvas.update()

def new_words():
    global words
    words = random.choice(to_learn)
    print(words)
    return

def tickfun():
    global words,timer
    window.after_cancel(timer)
    try:
        save_data()
    except:
        pass
    new_words()
    reset_card()
    timer = window.after(3000, func=flip_card)

def crossfun():
    global words, timer
    window.after_cancel(timer)
    new_words()
    reset_card()
    timer = window.after(3000, func=flip_card)


#-------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config()
window.title('Flash Cards')
window.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)
canvas = Canvas(width = 800, height = 526)
#images
BgCard = PhotoImage(file = 'images/card_back.png')
canvas.create_image(400,526/2, image = BgCard)
FgCard = PhotoImage(file = 'images/card_front.png')
card = canvas.create_image(400,526/2, image = FgCard)

tick_button_image = PhotoImage(file="images/right.png")
cross_button_image = PhotoImage(file="images/wrong.png")
canvas.config(bg = BACKGROUND_COLOR,highlightthickness=0)

canvas.grid(row = 0, column = 0, columnspan = 2)
#labels
card_title = canvas.create_text(400,150,text = 'Title', font = ('Ariel', 40 , 'italic'))
card_word = canvas.create_text(400,263,text='Word',font = ('Ariel',60,'bold'))
card_Counter = canvas.create_text(400,450,text=f'Remaining Cards: {len(to_learn)}',font = ('Ariel',20,'bold'))
#buttons
tickButton = Button(image=tick_button_image, highlightthickness=0,command = tickfun)
crossButton = Button(image=cross_button_image, highlightthickness=0, command = crossfun)
tickButton.grid(row = 1, column = 0)
crossButton.grid(row = 1, column = 1)

#-------------------------- LOOP ------------------------------- #

timer = window.after(3000, func=flip_card)
crossfun()
window.mainloop()