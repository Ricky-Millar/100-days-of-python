import random
from Data import data
from art import logo, vs
#start game



def game():
    choiceA = random.choice(data)
    choiceB = random.choice(data)
    game = True
    wins = 0
    while game == True:
        choiceB = random.choice(data)
        while choiceB == choiceA:
            choiceB = random.choice(data)

        #print graphics and data and stuff
        print(logo)
        print(f"Option A: {choiceA['name']}, a {choiceA['description']} from {choiceA['country']}")
        print (vs)
        print(f"Option B: {choiceB['name']}, a {choiceB['description']} from {choiceB['country']}.")

        #Take user imput
        if wins != 0:
            print("--------------------------------------")
            print(f"CORRECT! G0 AGAIN! you have won {wins} times!")
        print("--------------------------------------")
        Choice = input(" Who has the most followers?! A or B?:")
        Choice = str.lower(Choice)
        print("--------------------------------------")

        #Pull followers from data
        followersA = int(choiceA['follower_count'])
        followersB = int(choiceB['follower_count'])
        #check which is the winning score
        higherScore = max(followersA,followersB)
        #Check if winning score is the one chosen by the user
        if higherScore == followersA:
            winner = "a"
        else:
            winner = "b"
            choiceA = choiceB
        if Choice == winner:
            wins += 1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(logo)
            print("--------------------------------------------------")
            print (f"YOU LOOOOOOOOSE! you had a total of {wins} wins.")
            print("--------------------------------------------------")
            game = False
game()