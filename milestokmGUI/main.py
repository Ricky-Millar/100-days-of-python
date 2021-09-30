import tkinter
from tkinter import *
conversion = 0
def convert():
    global conversion
    conversion = int(input.get()) * 2
    result.config(text = conversion)
    return

window = Tk()

window.minsize(width= 50, height = 50)
window.title("Miles to Km")

button = Button(text = 'Convert', command = convert)
button.grid(column= 1, row = 3)

input = Entry()
input.grid(column = 1, row = 1)

title = Label(text = 'Miles to KM')
inputlable = Label(text = 'Convert:')
inputunit = Label(text = 'Miles')
resultunit = Label(text = 'KM')
result = Label(text = conversion)

title.grid(column = 1, row = 0)
inputlable.grid(column = 0, row =1 )
inputunit.grid(column = 2, row =1 )
resultunit.grid(column = 2, row =2 )
result.grid(column = 1, row =2 )



window.mainloop()