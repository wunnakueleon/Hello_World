print("Hello World!")

from turtle import Turtle, Screen
from snake import Snake
from food import Food, food_coordinates
from scoreboard import ScoreBoard
from grid_board import GridBoard, GRID_POSITION, VALID_POSITION, GRIDS
from bfs_pathfinding import BFS
import time

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor('black')

screen.tracer(0)



screen.title('Reverse Snake Game')

grid = GridBoard()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True
screen.listen()

food_placed = False
pick_fruit = False

def place_food(x, y):
    global food_placed
    global pick_fruit

    food.get_cor(x, y)
    food_pos = food.refresh(GRID_POSITION)

    if food_pos:
        snake_head_int = (int(snake.head.xcor()), int(snake.head.ycor()))
        
        snake.snake_path = snake.bfs.path_finding(snake_head_int, food_pos, VALID_POSITION, snake.segments)
        food_placed = True
        pick_fruit = True
        
    else:
        print("food_coordinates is empty!") 

screen.onclick(place_food)



while game_is_on:
    
    snake.move()

    if snake.head.distance(food) <= 14 and pick_fruit:
        food.hideturtle()
        snake.extend_segments()
        pick_fruit = False
        food_placed = False
        scoreboard.score_update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        for each_grid in GRIDS:
            each_grid.hideturtle()

        for each_segment in snake.segments:
            each_segment.hideturtle()
        game_is_on = False
 
    screen.update()
    time.sleep(0.1)
    
screen.mainloop()



