import random

gameStart = False

def runGame(guesses):
    number = random.randrange(1,100)
    while guesses != 0:
       # print(number) debug number
        guess = input("Guess a number!")
        if int(guess) == number:
            print(f"You Guessed it, the number was {number}. Congrats!")
            return "win"
        elif int(guess) > number:
            guesses -= 1
            print(f"Too High! you have {guesses} guesses left.")
        elif int(guess) < number:
            guesses -= 1
            print(f"Too Low! you have {guesses} guesses left.")
    return "loose"

def repeat():
    i=0
    global gameStart

    while i == 0:
        playAgain = input("Play again? y/n?")
        if playAgain == "y":
            return False
            i = 1
        elif playAgain == "n":
            return True
            i = 1
        else:
            print("Invalid Answer")

while gameStart == False:
    difficulty = input("Welcome to the number game!\n Would you like to play Easy or Hard?")
    if difficulty == "EASY":
        print (f"you {runGame(10)}!")
        gameStart = repeat()
    elif difficulty == "HARD":
        print(f"you {runGame(5)}!")
        gameStart = repeat()

    else:
        print("Try again, invalid answer!")
        print("----------------------------")

