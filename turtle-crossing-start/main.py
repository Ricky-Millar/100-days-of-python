import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
Car_Manager = CarManager()
player = Player()
screen.listen()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    scoreboard.write_score()
    Car_Manager.create_cars()
    Car_Manager.move_cars()
    screen.update()
    screen.onkey(key = 'Up', fun = player.go_up)
    for car in Car_Manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        if player.did_win():
            player.go_to_start()
            scoreboard.add_score()
            Car_Manager.level_up()


screen.exitonclick()