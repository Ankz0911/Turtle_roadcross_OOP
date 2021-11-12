from turtle import Turtle
from random import randrange, choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_cars(self):
        random_number = randint(1, 6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.goto(290, randrange(-220, 220, 10))
            new_car.left(180)
            new_car.shapesize(stretch_len=2)
            new_car.color(choice(COLORS))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT
