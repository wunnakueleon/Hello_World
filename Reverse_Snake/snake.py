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
        print(f"🐍 Path exists: {self.snake_path is not None}, Path length: {len(self.snake_path) if self.snake_path else 0}")
    
        if self.snake_path and len(self.snake_path) >= 1:  # Changed to >= 1
            for each_seg in range(len(self.segments) - 1, 0, -1):
                x_cor = self.segments[each_seg - 1].xcor()
                y_cor = self.segments[each_seg - 1].ycor()
                self.segments[each_seg].goto(x_cor, y_cor)

            if len(self.snake_path) > 1:
                # Calculate direction when we have a next position
                current_pos = self.snake_path[0]
                next_pos = self.snake_path[1]

                dx = next_pos[0] - current_pos[0]
                dy = next_pos[1] - current_pos[1]

                print(f"Current: {current_pos}, Next: {next_pos}")
                print(f"dx={dx}, dy={dy}, old_direction={self.head_direction}")
                
                if dx > 0:
                    self.head_direction = 0
                elif dx < 0:
                    self.head_direction = 180
                elif dy > 0:
                    self.head_direction = 90
                elif dy < 0:
                    self.head_direction = 270

                print(f"is heading updated?{self.head_direction}")
                self.head.goto(next_pos)
            else:
                # Just move to the last position without updating direction
                print(f"🎯 Final position: {self.snake_path[0]}")
                self.head.goto(self.snake_path[0])
        
            self.snake_path.pop(0)

            if len(self.snake_path) == 0:
                print("🎯 Path is now empty, setting to None")
                self.snake_path = None
       

        else:
            # No path - move straight in grid-aligned way
            print(f"➡️ Moving straight! Direction: {self.head_direction}")
            
            for each_seg in range(len(self.segments) - 1, 0, -1):
                x_cor = self.segments[each_seg - 1].xcor()
                y_cor = self.segments[each_seg - 1].ycor()
                self.segments[each_seg].goto(x_cor, y_cor)
            
            # Calculate next grid position based on direction
            current_x = int(self.head.xcor())
            current_y = int(self.head.ycor())
            
            if self.head_direction == 0:  # East
                next_pos = (current_x + 20, current_y)
            elif self.head_direction == 180:  # West
                next_pos = (current_x - 20, current_y)
            elif self.head_direction == 90:  # North
                next_pos = (current_x, current_y + 20)
            elif self.head_direction == 270:  # South
                next_pos = (current_x, current_y - 20)
            else:
                # Default to East if direction is weird
                next_pos = (current_x + 20, current_y)
            
            print(f"➡️ Moving from ({current_x}, {current_y}) to {next_pos}")
            self.head.goto(next_pos)
