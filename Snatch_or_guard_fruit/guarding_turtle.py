from fruit import Fruit
# Guard the fruit and catch the snatcher


class Guardian(Fruit):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('blue')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(Fruit.random_x_fruit + 50, Fruit.random_y_fruit)

    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)

    def turn_right(self):
        self.right(10)

    def turn_left(self):
        self.left(10)
