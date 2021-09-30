from replit import clear #### THIS WILL NOT WORK HERE
from art import logo
#HINT: You can call clear() to clear the output in the console
bidders = {}
bidding = True
print(logo)
while bidding == True:
  bidderName = input("What is your name?\n")
  clear()
  print(logo)
  bid = input ("What is your bid?\n$")
  clear()
  print(logo)
  bidders[bidderName] = bid
  answer = input("Are there any other bidders, type yes or no  \n")
  clear()
  print(logo)
  if answer != "yes":
    if answer == "no":
      bidding = False
    else:
      print("invalid answer")
previous_bid = 0
for i in bidders:
  current_bid = bidders[i]
  if int(current_bid) > int(previous_bid):
    winner = i
    winning_bid = bidders[i]
  previous_bid = current_bid

print(f"{winner} won with a bid of ${winning_bid}")