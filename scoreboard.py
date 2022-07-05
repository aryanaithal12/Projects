from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(-280, 260)
        self.write(f"Level : {self.level}", move=False, align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align='center', font=FONT)
