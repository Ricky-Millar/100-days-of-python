# Step 1
import random

import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
word_length = len(chosen_word)
lives = 6
game = 0
blank = []
for letter in chosen_word:
    blank.append("_")
blankTemp = list(blank)
previousGuess = []

while game == 0:

    guess = input("Guess a letter").lower()

    if guess in previousGuess:
        print("Guess Again!")
    else:
        previousGuess.append(guess)
        print(previousGuess)
        word = []
        i = 0
        blankTemp = list(blank)
        for letter in chosen_word:
            if guess == letter:
                blank[i] = letter

            i += 1

        print(blank)

        if blank == blankTemp:
            lives -= 1
        else:
            print(f"{guess} Is in the word!")
        print(hangman_art.stages[lives])
        if "_" not in blank:
            game = 1
        if lives == 0:
            game = 1
if lives == 0:
    print("YOU LOSE")
else:
    print("YOU WIN!")
