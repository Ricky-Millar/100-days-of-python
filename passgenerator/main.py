#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

PassLen = 0
password = []
finalPass = ""
for let in range(0 , nr_letters):
    PassLen += 1
    password.insert(random.randrange(0, PassLen), random.choice(letters))

for num in range(0 , nr_symbols):
    PassLen += 1
    password.insert(random.randrange(0, PassLen), random.choice(symbols))


for sym in range(0 , nr_numbers):
    PassLen += 1
#    Incrementing passlen lets the program track how long the password is, so it can then chose a random spot within that range to put in new chars
    password.insert(random.randrange(0, PassLen), random.choice(numbers))
#   ^inserts into password ^ at a random point in its length ^ a random choice from the list numbers

for x in password:
    finalPass += x

print (f"Your password is {finalPass}")
# Notes - improvements
# Instead of using a custom loop to randomly insert chars, you can use random.shuffle(list) to shuffle a un-random list
