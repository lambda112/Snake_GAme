import turtle as t
from time import sleep

# Setup Screen
screen = t.Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Create Snake Body
starting_positions = [(0,0), (-20,0), (-40, 0)]
segments = [] 

for position in starting_positions:
    new_segment = t.Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# Animate Snake
game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)


# Close on Click
screen.exitonclick()