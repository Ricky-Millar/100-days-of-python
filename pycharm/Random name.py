# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# f lets you insert non strings into the {}, len-1 as the list counts from 0 and the length counts from 1. 
print( f"{names[random.randint(0, len(names)-1)]} is going to buy the meal today.")
