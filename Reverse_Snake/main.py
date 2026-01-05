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
    print("🔄 Loop iteration starting...")
    snake.move()

    if snake.head.distance(food) <= 14 and pick_fruit:
        print("🍎 About to eat food and extend!")
        food.hideturtle()
        print("🍎 Food hidden")
        snake.extend_segments()
        print("🍎 Snake extended")  # ← Does this print?
        pick_fruit = False
        food_placed = False
        scoreboard.score_update()
        print("🍎 Score updated")
        snake.snake_path = None
        print("🍎 Path cleared to prevent collision")

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        
        for each_grid in GRIDS:
            each_grid.hideturtle()

        for each_segment in snake.segments:
            each_segment.hideturtle()
        game_is_on = False
        food.hideturtle()
        scoreboard.game_over()

    for each_segment in snake.segments[1:]:
        if snake.head.distance(each_segment) <= 14:
            print(f"💥 COLLISION! Head at ({snake.head.xcor()}, {snake.head.ycor()})")
            print(f"💥 Collided with segment at ({each_segment.xcor()}, {each_segment.ycor()})")
            print(f"💥 Distance: {snake.head.distance(each_segment)}")
            # Hide everything FIRST (same as wall collision)
            for each_grid in GRIDS:
                each_grid.hideturtle()
            for each_segment in snake.segments:
                each_segment.hideturtle()
            game_is_on = False
            food.hideturtle()
            scoreboard.game_over()

    print(len(snake.segments))
 
    screen.update()
    time.sleep(0.1)
    
screen.mainloop()



