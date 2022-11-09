from turtle import Turtle
from random import choice, randint

color_list = ["red", "green", "blue", "purple", "pink", "orange", "violet", "cyan",
              "yellow", "lightgreen", "skyblue", "grey"]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.spawn(randint(15, 20))
        self.move_speed = 6

    def spawn(self, num_of_cars):
        for i in range(num_of_cars):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(color_list))
            new_car.penup()
            new_car.goto(randint(-280, 280), randint(-200, 200))
            self.car_list.append(new_car)

    def respawn(self):
        for car in self.car_list:
            if car.xcor() < -320:
                car.color(choice(color_list))
                car.goto(x=320, y=randint(-200, 200))

    def move(self):
        for car in self.car_list:
            car.setheading(180)
            car.forward(self.move_speed)

