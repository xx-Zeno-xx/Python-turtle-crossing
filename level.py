from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-240, y=260)
        self.game_level = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.game_level}", align="center", font=("Bold", 20, "normal"))

    def increase_level(self):
        self.game_level += 1
        self.refresh()

    def game_over(self):
        self.game_level = 1
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Bold", 20, "normal"))
