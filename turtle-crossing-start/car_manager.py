from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def create_cars(self):

        if random.randint(1,6) == 6:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1,stretch_len=4)
            new_car.penup()
            color = random.choice(COLORS)
            new_car.color(color)
            random_y = random.randint(-250,250)
            new_car.goto(x=300, y= random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
                car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


