from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.go_to_start()
        self.left(90)


    def moving_turtle(self):
        self.forward(MOVE_DISTANCE)


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def next_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False