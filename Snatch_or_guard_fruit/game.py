from turtle import Screen
from fruit import Fruit
from guarding_turtle import Guardian
from snatching_turtle import Snatcher
from shooting_turtle import Shooter, Cannon
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

fruit = Fruit()
fruit.fruit_entity()
guardian = Guardian()
snatcher = Snatcher()
shooter = Shooter()
cannons = Cannon()

screen.listen()
screen.onkey(snatcher.move_forward, "Up")
screen.onkey(snatcher.move_backward, "Down")
screen.onkey(snatcher.turn_right, "Right")
screen.onkey(snatcher.turn_left, "Left")

screen.onkey(guardian.move_forward, "w")
screen.onkey(guardian.move_backward, "s")
screen.onkey(guardian.turn_right, "d")
screen.onkey(guardian.turn_left, "a")

screen.onkey(shooter.turn_left, "l")
screen.onkey(shooter.turn_right, "j")
screen.onkey(cannons.shoot_cannon, "space")

fruit.fruit_entity()
cannon_refills = []

while True:
    time.sleep(0.1)
    cannons.move_ball()
    cannons.change_direction(shooter, shooter.turn_right, shooter.turn_left)
    time.sleep(0.01)

    if snatcher.xcor() > 395 or snatcher.xcor() < -395:
        snatcher.color('red')
        snatcher.goto(0, 0)
        screen.clear()
        snatcher.write("The Red Turtle has lost! Hitting the wall", align="center", font=("Arial", 24, "bold"))
        break

    elif snatcher.ycor() > 290 or snatcher.ycor() < -290:
        snatcher.color('red')
        snatcher.goto(0, 0)
        screen.clear()
        snatcher.write("The Red Turtle has lost! Hitting the wall", align="center", font=("Arial", 24, "bold"))
        break

    elif guardian.xcor() > 395 or guardian.xcor() < -395:
        guardian.color('red')
        guardian.goto(0, 0)
        screen.clear()
        guardian.write("The Red Turtle has lost! Hitting the wall", align="center", font=("Arial", 24, "bold"))
        break

    elif guardian.ycor() > 290 or guardian.ycor() < -290:
        guardian.color('red')
        guardian.goto(0, 0)
        screen.clear()
        guardian.write("The Red Turtle has lost! Hitting the wall", align="center", font=("Arial", 24, "bold"))
        break

    elif snatcher.distance(cannons) < 15:
        cannons.color('yellow')
        cannons.goto(0, 0)
        screen.clear()
        cannons.write("You have been hit!", align='center', font=('Arial', 24, 'bold'))
        break

    elif snatcher.distance(fruit) < 17:
        fruit.goto(0, 0)
        screen.clear()
        fruit.color('red')
        fruit.write("Fruit taken!!", align='center', font=('Arial', 24, 'bold'))
        break

    elif snatcher.distance(guardian) < 17:
        guardian.goto(0, 0)
        screen.clear()
        guardian.color('blue')
        guardian.write("Caught by the guard!", align='center', font=('Arial', 24, 'bold'))
        break

    elif guardian.distance(fruit) < 30:
        guardian.setheading(guardian.towards(fruit) + 180)
        guardian.forward(20)

    screen.update()

screen.exitonclick()
