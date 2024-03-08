import turtle as t
from time import sleep
from snake import Snake

# Setup Screen
screen = t.Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Move Snake
snake = Snake()
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

# Close on Click
screen.exitonclick()