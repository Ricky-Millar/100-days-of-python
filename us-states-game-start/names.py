import pandas
from turtle import Turtle
class UsNames(Turtle):
    def __init__(self):
        super().__init__()
        self.us_list = pandas.read_csv('50_states.csv')
        self.state_list = self.us_list.state.to_list()

    def name_on_list(self,user_guess):
        for name in self.state_list:
            if name == user_guess:
                x = self.us_list[self.us_list.x == user_guess]
                y = self.us_list[self.us_list. == user_guess]
                cords = [x,y]
                return cords
        return 'boobies'
