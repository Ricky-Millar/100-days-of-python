from tkinter import *
from playground import add
window = Tk()
window.title('My First GUI, thanks bro')
window.minsize(width=500, height=300)
def buttonclick():
    my_label.config(text=input.get())
window.config(padx=20, pady=20)
my_label = Label(text='I am a Label',font=('Arial',24, "bold"))
my_label.grid(column = 1, row = 1)
my_button = Button(text = "Click Me" ,command = buttonclick)
my_button.grid(column= 2, row = 2)
my_button2 = Button(text = "Click Me" ,command = buttonclick)
my_button2.grid(column= 3, row = 1)
input = Entry(width= 10)
input.grid(column = 4, row = 3)
input.get()





print(add(1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17))
















window.mainloop() #Needs to be at end of program