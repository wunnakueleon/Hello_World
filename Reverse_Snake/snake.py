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

            next_pos = self.snake_path[1]
            self.head.goto(next_pos) 

            self.snake_path.pop(0)    
        else:
            print("Snake path not moving")    

            

    

            

    
        
        
        

