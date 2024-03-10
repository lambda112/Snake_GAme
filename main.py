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
food = Food(screen_width=screen.window_width(), screen_height=screen.window_height())

# Game Loop
game_is_on = True
food.create_food()
screen = t.Screen()
screen.listen()
screen.onkeypress(fun = snake.upward, key = "w")
screen.onkeypress(fun = snake.downward, key = "s")
screen.onkeypress(fun = snake.left, key = "a")
screen.onkeypress(fun = snake.right, key = "d")
        

while game_is_on:
    snake.move()
    screen.update()
    sleep(0.085)

    if food.check_collision(snake_pos= snake.get_postion()):
        snake.segments.append(snake.create_segment(snake.new_pos))
        snake.new_cord_value - 20

# Close on Click
screen.exitonclick()