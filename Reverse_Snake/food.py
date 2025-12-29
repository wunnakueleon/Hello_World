from turtle import Turtle
import random 


food_coordinates = ()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def get_cor(self, x_cor, y_cor):
        global food_coordinates
        food_coordinates = (x_cor, y_cor)
        return food_coordinates
        
    def refresh(self, grid_positions):
        global food_coordinates
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

        if not food_coordinates:
            self.hideturtle()
            return 
        
        user_x, user_y = food_coordinates

        match_found = False
        for position in grid_positions:
            self.showturtle()
            x, y = position
            if (x - 10 <= user_x <= x + 10) and (y - 10 <= user_y <= y + 10):
                self.goto(x, y)
                food_coordinates = (x, y)
                return (x, y)
                
                
        




