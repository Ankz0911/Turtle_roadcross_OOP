import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.move_turtle, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_cars()
    car_manager.move_cars()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            player.restart_turtle()
    if player.ycor() == 280:
        scoreboard.increase_score()
        car_manager.increase_level()
        player.restart_turtle()

screen.exitonclick()
