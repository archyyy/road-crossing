from turtle import Screen
from time import sleep
from player import Player
from cars import Obstacle
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = Obstacle()
scoreboard = Scoreboard()

# Keys input
screen.listen()
screen.onkeypress(player.move, 'w')

car_speed = 10
gaming = True
while gaming:
    sleep(0.1)
    cars.respawn_cars()
    cars.move_cars(car_speed)

    # Colision detection
    for car in cars.cars:
        if player.distance(car) < 25:
            gaming = False   
            scoreboard.gameover()

    # Win condition        
    if player.ycor() > 270:
        # Reset position and speed up
        player.reset_position()
        car_speed += 5 
        scoreboard.point()

    screen.update()

screen.exitonclick()


