from turtle import Turtle
from fruit import Fruit

# Creating a shooter to blast open the snatcher!!


class Shooter(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('yellow')
        self.penup()
        self.goto(-370, 230)
        self.heading()

    def turn_right(self):
        self.right(10)

    def turn_left(self):
        self.left(10)


class Cannon(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(-350, 230)
        self.dx = 10
        self.dy = 10
        self.shooting_cannon = False
        self.cannon_shot = False

    def shoot_cannon(self):
        self.shooting_cannon = True
        self.cannon_shot = True

    def change_direction(self, shooter_reference, turn_right_shooter, turn_left_shooter):
        if not self.cannon_shot:
            self.setheading(shooter_reference.heading())
            turn_right_shooter()
            if turn_right_shooter():
                self.xcor() - self.dx
                self.ycor() - self.dy
            turn_left_shooter()
            if turn_left_shooter():
                self.xcor() + self.dx
                self.ycor() + self.dy

    def new_cannons(self):
        self.hideturtle()  # Hide the cannonball for reset
        self.goto(-350, 230)  # Reset position
        self.shooting_cannon = False  # Reset shooting state
        self.showturtle()

    def move_ball(self):
        if self.shooting_cannon:
            if self.heading() == 0 or self.heading() == 360:
                self.setx(self.xcor() + self.dx)

            elif self.heading() == 180:
                self.sety(self.xcor() - self.dx)

            elif self.heading() == 270:
                self.sety(self.ycor() - self.dy)

            elif self.heading() == 90:
                self.sety(self.ycor() + self.dy)

            elif 270 < self.heading() < 360:
                self.setx(self.xcor() + self.dx)
                self.sety(self.ycor() - self.dy)

            elif 180 < self.heading() < 270:
                self.setx(self.xcor() - self.dx)
                self.sety(self.ycor() - self.dy)

            elif 0 < self.heading() < 90:
                self.setx(self.xcor() + self.dx)
                self.sety(self.ycor() + self.dy)

            elif 90 < self.heading() < 180:
                self.setx(self.xcor() - self.dx)
                self.sety(self.ycor() + self.dy)

            self.check_frames()

    def check_frames(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.change_y()

        if self.xcor() > 385 or self.xcor() < -385:
            self.change_x()

    def change_x(self):
        self.dx *= -1

    def change_y(self):
        self.dy *= -1
