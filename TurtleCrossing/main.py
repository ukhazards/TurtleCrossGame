import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(turtle.moving_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()


    for car in car_manager.all_cars:
         if car.distance(turtle) < 20:
             game_is_on = False
             scoreboard.game_over()

    if turtle.next_level():
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()