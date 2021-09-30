from turtle import Turtle, Screen
import pandas, names
us_list = pandas.read_csv('50_states.csv')
# map = Screen()
# map.screensize(canvwidth=725,canvheight=492)
# map.bgpic('blank_states_img.gif')
NameMachine = names.UsNames()
print(NameMachine.name_on_list(user_guess='Alabama'))




# map.exitonclick()