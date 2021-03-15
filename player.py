from turtle import Turtle

SPEED = 10

class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-270)

    
    def move(self):
        self.forward(SPEED)

    
    def reset_position(self):
        self.goto(x=0, y=-270)