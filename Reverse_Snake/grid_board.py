from turtle import Turtle

# For each Quadrant
ROW_DISTANCE_BLOC = 20
COLUMN_DISTANCE_BLOC = 20

class GridBoard():

    def __init__(self):
        self.fill_up_grid()

    def create_bloc(self, position):
        self.new_bloc = Turtle("square")
        self.new_bloc.color("white")
        self.new_bloc.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.new_bloc.penup()
        self.new_bloc.goto(position)

    def fill_up_grid(self):
        # For First Quadrant
        x_distance = 0
        y_distance = 0

        for each_row in range(15):
            for each_column in range(15):
                x_distance += 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance += 20
            
        x_distance = 0
        y_distance = 0
        # For Second Quadrant
        for each_row in range(15):
            for each_column in range(15):
                x_distance -= 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance += 20
            

        # For Third Quadrant
        x_distance = 0
        y_distance = 0

        for each_row in range(15):
            for each_column in range(15):
                x_distance -= 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance -= 20

        # For Fourth Quadrant
        x_distance = 0
        y_distance = 0

        for each_row in range(15):
            for each_column in range(15):
                x_distance += 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance -= 20

        # For middle lane where 0, 0 is missing
        x_distance = 0
        y_distance = 280

        for each_row in range(29):
            position = (x_distance, y_distance)
            self.create_bloc(position)
            x_distance = 0
            y_distance -= 20





