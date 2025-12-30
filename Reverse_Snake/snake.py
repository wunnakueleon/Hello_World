from turtle import Turtle
from bfs_pathfinding import BFS
from food import food_coordinates
from grid_board import VALID_POSITION

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():

    def __init__(self):
        self.segments = []
        self.segment_position = []
        self.create_snake()
        self.head = self.segments[0]
        self.bfs = BFS()
        self.snake_path = None
        self.head_direction = self.head.heading()
        

    def create_snake(self):
        for each_position in POSITION:
            self.add_segments(each_position)
            
    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(position)
        self.segment_position.append(new_segment.position())
        self.segments.append(new_segment)

    def extend_segments(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        if self.snake_path and len(self.snake_path) > 1:
            for each_seg in range(len(self.segments) - 1, 0, -1):
                    x_cor = self.segments[each_seg - 1].xcor()
                    y_cor = self.segments[each_seg - 1].ycor()
                    self.segments[each_seg].goto(x_cor, y_cor)

            current_pos = self.snake_path[0]
            next_pos = self.snake_path[1]

            dx = next_pos[0] - current_pos[0]
            dy = next_pos[1] - current_pos[1]
            
            if dx > 0:
                self.head_direction = 0    # Moving East
            elif dx < 0:
                self.head_direction = 180  # Moving West
            elif dy > 0:
                self.head_direction = 90   # Moving North
            elif dy < 0:
                self.head_direction = 270  # Moving South

            print(f"is heaidng updated?{self.head_direction}")
            self.head.goto(next_pos) 
            self.snake_path.pop(0)    
        else:
            for each_seg in range(len(self.segments) - 1, 0, -1):
                    x_cor = self.segments[each_seg - 1].xcor()
                    y_cor = self.segments[each_seg - 1].ycor()
                    self.segments[each_seg].goto(x_cor, y_cor)
            self.head.setheading(self.head_direction)
            self.head.forward(MOVE_DISTANCE)

            

    

            

    
        
        
        

