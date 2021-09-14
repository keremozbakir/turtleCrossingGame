import time
from turtle import Screen, Turtle
from player import Player
from car import Car
from car_manager import CarManager
from scoreboard import Scoreboard
import random

y_coordinate = random.randint(-250, 250)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car = Car()
car.hideturtle()
screen.listen()

screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    if player.ycor() > 280:
        player.success_cross()
        car.level_up()
        scoreboard.level_up()
        scoreboard.update_scoreboard()

    for item in car.all_cars:
        if item.distance(player) < 22:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
