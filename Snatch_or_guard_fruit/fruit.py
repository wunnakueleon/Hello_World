from turtle import Turtle
import random
# Creating the fruit


class Fruit(Turtle):
    random_x_fruit = random.randint(-300, -190)
    random_y_fruit = random.randint(-250, 200)
    random_position = (random_x_fruit, random_y_fruit)

    def __init__(self):
        super().__init__()

    def fruit_entity(self):
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color(random.choice(["cyan", "green", "yellow", "purple", "orange"]))
        self.penup()
        self.goto(Fruit.random_position)
        self.draw_protection_rim()

    def draw_protection_rim(self):
        rim = Turtle()
        rim.penup()
        rim.goto(self.xcor(), self.ycor() - 25)
        rim.pendown()
        rim.color('gold')
        rim.pensize(3)
        rim.circle(25)
        rim.hideturtle()
