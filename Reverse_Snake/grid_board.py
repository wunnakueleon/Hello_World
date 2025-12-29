from turtle import Turtle

# For each Quadrant
ROW_DISTANCE_BLOC = 20
COLUMN_DISTANCE_BLOC = 20

GRID_POSITION = []
VALID_POSITION = set()

class GridBoard():

    def __init__(self):
        self.fill_up_grid()

    def create_bloc(self, position):
        self.new_bloc = Turtle("square")
        self.new_bloc.color("white")
        self.new_bloc.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.new_bloc.penup()
        GRID_POSITION.append(position)
        self.new_bloc.goto(position)
        global VALID_POSITION
        VALID_POSITION.add((0, 0))
        VALID_POSITION.add(position)

    def fill_up_grid(self):

        # For First Quadrant
        x_distance = 0
        y_distance = 0

        for each_row in range(15):
            for each_column in range(14):
                x_distance += 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance += 20
            
        # For Second Quadrant
        x_distance = 0
        y_distance = 0

        for each_row in range(15):
            for each_column in range(14):
                x_distance -= 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance += 20
            

        # For Third Quadrant
        x_distance = 0
        y_distance = 0

        for each_row in range(15):
            for each_column in range(14):
                x_distance -= 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance -= 20

        # For Fourth Quadrant
        x_distance = 0
        y_distance = 0

        for each_row in range(15):
            for each_column in range(14):
                x_distance += 20
                position = (x_distance, y_distance)
                self.create_bloc(position)
            x_distance = 0
            y_distance -= 20

        # For middle lane where 0, 0 is missing
        x_distance = 0
        y_distance = 300

        for each_row in range(29):
            x_distance = 0
            y_distance -= 20
            position = (x_distance, y_distance)
            self.create_bloc(position)
            
        return VALID_POSITION





