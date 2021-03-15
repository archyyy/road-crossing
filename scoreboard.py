from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 240)
        self.write(self.score, align="center", font=("Courier", 30, "normal"))


    def point(self):
        self.score += 1
        self.update_scoreboard()


    def gameover(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.write('GAME OVER', align="center", font=("Courier", 40, "normal"))
