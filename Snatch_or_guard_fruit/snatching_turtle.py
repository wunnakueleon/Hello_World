from turtle import Turtle
import random
# Creating a snatcher turtle to steal the fruit


class Snatcher(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto(random.randint(150, 360), random.randint(-260, 260))
        self.setheading(180)

    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)

    def turn_right(self):
        self.right(10)

    def turn_left(self):
        self.left(10)
