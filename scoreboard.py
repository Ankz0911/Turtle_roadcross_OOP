from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(self.score, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER , Your score is {self.score}', align=ALIGN, font=FONT)
