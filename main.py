import turtle as t
from time import sleep
from snake import Snake
from food import Food

# Setup Screen
screen = t.Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Instinate Objects
snake = Snake()
food = Food(screen_width=screen.window_width(), screen_height=screen.window_height(), snake_pos=snake.get_postion())

# Game Loop
game_is_on = True
food.create_food()

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    food.check_collision()

# Close on Click
screen.exitonclick()