from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        new_y = self.ycor() + 15
        self.goto(x=self.xcor(), y=new_y)

    def reset_turtle(self):
        self.goto(x=0, y=-280)

