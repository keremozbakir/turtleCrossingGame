from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.moving_distance = 10
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            # print(self.cars)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # print(self.xcor())

    def level_up(self):

        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)
