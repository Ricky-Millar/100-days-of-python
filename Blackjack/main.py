import random

from art import logo
from cards import deck

playerHand = []
botHand = []
cardValue = 0
gameState = 0  # 0 is draw 1 is you win 2 is bot wins


def randomCard():
    card = random.choice(list(deck))
    return card

# Could have used sum.(hand)
def sumHand(hand):
    total = 0
    for i in hand:
        total += int(deck[i])
    return total

def resultText():
    print(f"Your final hand was:\n{createHandText(playerHand)} \ntotaling: {playerSum}\n")
    print(f"bots final hand was:\n{createHandText(botHand)} \ntotaling: {botSum}\n")
    print('-------------------------------------------------------\n')

def initialDraw():
    playerHand.append(randomCard())
    playerHand.append(randomCard())
    botHand.append(randomCard())
    print(f"Your cards are '{playerHand[0]}' and '{playerHand[1]}' totaling: {sumHand(playerHand)}")
    print(f"Bots first card: {botHand[0]}")
    print('\n-------------------------------------------------------\n')



def createHandText(hand):
    text = ''
    for i in hand:
        text += str(i) + ", "
    return text


# EG HOW TO SELECT A CARD AND ITS VALUE
# Card = randomCard()
# cardValue=deck[Card]
# print(f"{Card} {cardValue}")

if input("Do you want to play a game of blackjack y/n?") == "y":
    gamePlay = True
    print(logo)
    initialDraw()

while gamePlay == True:

    if input("do you want to draw another card, y/n?") == "y":

        playerHand.append(randomCard())
        playerSum = sumHand(playerHand)
        botSum = sumHand(botHand)
        if botSum <= random.randrange(8, 18):
            botHand.append(randomCard())

        if botSum >= 22 and playerSum >= 22:
            print("You both cooked it!")
            resultText()
            gamePlay = False
        elif playerSum >= 22:
            print("You cooked it!")
            resultText()
            gamePlay = False
        elif botSum >= 22:
            print("You win!")
            resultText()
            gamePlay = False
        else:
            print(f"Your cards are: {createHandText(playerHand)} totaling: {playerSum}")
            print(f"Bots first card: {botHand[0]}")
            print('-------------------------------------------------------\n')
