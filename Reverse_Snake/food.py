from turtle import Turtle
import random 

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_list = list(range(20, 290, 20))
        random_x = random.choice(x_list)
        y_list = list(range(20, 290, 20))
        random_y = random.choice(y_list)
        self.goto(random_x, random_y)




