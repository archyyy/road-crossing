from turtle import Turtle
from random import choice, randint
from time import sleep
CAR_COLORS = ['red', 'blue', 'purple', 'green', 'yellow', 'orange', 'pink']


class Obstacle():


    def __init__(self):
        self.cars = []


    def respawn_cars(self):
        respawn_chance = randint(1, 5)
        if respawn_chance == 1:
            car = Turtle()
            x_cor = 300
            y_cor = randint(-240, 240)
            car.shape('square')
            car.penup()
            car.shapesize(stretch_len=2)
            car.setheading(180)
            car.color(choice(CAR_COLORS))
            car.goto(x_cor, y_cor)
            self.cars.append(car)

    
    def move_cars(self, car_speed):
        for car in self.cars:
            car.forward(car_speed)

