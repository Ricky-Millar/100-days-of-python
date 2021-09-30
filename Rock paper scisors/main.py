import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Moves = [rock,paper,scissors]

playerMove = int(input("Press 1 for rock, 2 for paper and 3 for scissors. ")) - 1

botMove = random.randint(0, 2)

print("-----PLAYER-----" + Moves[playerMove])
print("-----BOT-----" + Moves[botMove])

if playerMove == 0:
    if botMove == 1:
        print("YOU LOSE")
    elif botMove == 2:
        print("YOU WIN")
    else:
        print("DRAW")

if playerMove == 1:
    if botMove == 2:
        print("YOU LOSE")
    elif botMove == 0:
        print("YOU WIN")
    else:
        print("DRAW")

if playerMove == 2:
    if botMove == 0:
        print("YOU LOSE")
    elif botMove == 1:
        print("YOU WIN")
    else:
        print("DRAW")



