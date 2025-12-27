print("Hello World!")

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from grid_board import GridBoard
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
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_update()
        snake.extend_segments()

    # Detect collision with wall
    if (snake.head.xcor() < -280) or (snake.head.xcor() > 280) or (snake.head.ycor() < -280) or (snake.head.ycor() > 280):
        scoreboard.clear()
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with the body
    for every_seg in snake.segments[1:]:
        if (snake.head.distance(every_seg.position()) <= 10):
            scoreboard.game_over()
            game_is_on = False

    screen.update()
    time.sleep(0.05)
    
screen.exitonclick()



