import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle crossing')
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.move_up, 'w')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # TODO: create new car

    cars.new_car()

    # TODO: detect collision with the car
    for car in cars.car_list:
        if player.distance(car) < 20:
            score.game_over()
            screen.update()
            game_is_on = False

    # TODO: Detect if the player finished the level
    if player.finish():
        cars.next_level()
        player.refresh()
        score.update_score()
    cars.move()

screen.exitonclick()
