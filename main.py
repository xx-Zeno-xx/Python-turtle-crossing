from turtle import Turtle, Screen
from player import Player
import time
from cars import Cars
from level import Level
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
car = Cars()
my_turtle = Player()
screen.listen()
screen.onkey(fun=my_turtle.move_up, key="w")
level = Level()
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    if my_turtle.ycor() > 300:
        level.increase_level()
        my_turtle.reset_turtle()
        car.move_speed += 2
    car.move()
    car.respawn()
    for cars in car.car_list:
        if my_turtle.distance(cars) < 20:
            is_on = False
            level.game_over()





screen.exitonclick()