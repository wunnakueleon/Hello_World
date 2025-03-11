"""
Functions and features:
First, create three turtles: snatching turtle(the red turtle), guarding turtle(the blue turlte) and cannon-shooting turtle(the yellow turtle)
- Snatching turtle will be snatching the food, (obviously)
- Guarding turtle will guard the fruit from being snatched
- Cannon-shooting turtle will shoot cannon at the press of a button("the space bar").

Controls:
The snatcher can be controlled using the keys "Up", "Down", "Right", "Left".
The guard can be controlled by keys: "w" for move_forward, "s" for move_backward, "a" for turn_left and "d" for turn_right.
The shooter is stationary, but it controls the cannon ball's direction with "l" to move left and "j" to move right, and then "the space bar" to shoot the ball.

Area to note of:
-The guard cannot enter the radius protective layer of the fruit. Because the guard can station itself on top of the fruit, and so the snatcher 
will not be able to snatch the fruit because it will touch the guard and it will be the end of the game for the red turtle.

-Although the cannon ball isn't moved alongside the shooter, its direction is determined by the shooter's direction to shoot off. 
Once shot, the ball will be bouncing on four sides.

Conditions:
If the snatcher gets hit by the ball, it's GAME OVER.
If the snatcher gets the fruit, it's GAME OVER.
If the guard grasps the snatcher, it's GAME OVER.
"""
