from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
USERNAME = 'Ricky.j.millar@gmail.com'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passGen():

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(END, "".join(password_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePass():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
        'username': username,
        'Password': password,
    }
    }
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title= 'oops', message = 'You did not complete all the boxes!')
    else:
        try:
            with open("passwords.json", "r") as passLog:
                data = json.load(passLog) #Load data from file and store it as a dictionary
        except FileNotFoundError:
            with open("passwords.json", "w") as passLog:
                json.dump(new_data, passLog, indent=4)
                print('creating new file')
        else:
            data.update(new_data)  # updates the dictuinary with json format
            with open("passwords.json", "w") as passLog:
                json.dump(data, passLog, indent = 4) # saves new dictionady back into json file
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0,'end')
#---------------------------Pass Search------------------------------#
def passSearch():
    try:
        with open('passwords.json', "r") as passLog:
            try:
                website = website_entry.get()
                data = json.load(passLog)
                username = data[website]['username']
                password = data[website]['Password']
                print(username)
                messagebox.showinfo(message=f"Website: {website},\n`Username: {username},\nPassword:{password}")
            except KeyError:
                messagebox.showwarning(message="Website not found")
    except:
        messagebox.showwarning(message="no saved passwords")




#-------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx = 50, pady = 50)
canvas = Canvas(width = 200, height = 200)
#Image
LockImg = PhotoImage(file = 'logo.png')
canvas.create_image(100,100, image = LockImg)
canvas.grid(row = 0, column = 1)
#lables
website_label = Label(text = 'Website:')
username_label = Label(text = 'Email/Username:')
password_label = Label(text = 'Password:')
#debug_label = Label(text = '[Debug]:')

website_label.grid(row=1, column = 0)
username_label.grid(row=2, column = 0)
password_label.grid(row=3, column = 0)
#debug_label.grid(row = 6, column = 2, sticky = W)

#entry
website_entry = Entry(width = 32)
website_entry.focus()
username_entry = Entry(width = 53)
username_entry.insert(END, USERNAME)
password_entry = Entry(width = 32)

website_entry.grid(row=1, column = 1, columnspan = 2,sticky = W)
username_entry.grid(row=2, column = 1, columnspan = 2 , sticky = W)
password_entry.grid(row=3, column = 1, sticky = W)
#button
generate_password_button = Button(text = 'Generate Password', padx = 5, command=passGen)
search_button = Button(text = 'Password Search', padx = 5, command=passSearch)
add_button = Button(text = 'Add', width = 45 , command = savePass)

generate_password_button.grid(row = 3, column = 2 )
search_button.grid(row = 1, column = 2 , sticky = 'W')
add_button.grid(row = 4 , column = 1, columnspan = 2)



window.mainloop()