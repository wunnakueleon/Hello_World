print("Hello World!")

from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Reverse Snake Game')

snake = Snake()

screen.tracer(0)


screen.update()
screen.exitonclick()



