from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            timmy = Turtle(shape='square')
            timmy.shapesize(stretch_wid=1, stretch_len=2)
            timmy.color(random.choice(COLORS))
            timmy.penup()
            timmy.setheading(180)
            timmy.goto(300, random.randint(-230, 230))
            self.car_list.append(timmy)

    def move(self):
        for tim in self.car_list:
            tim.fd(self.move_distance)

    def next_level(self):
        self.move_distance += MOVE_INCREMENT
