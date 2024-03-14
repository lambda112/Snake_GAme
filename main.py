import turtle as t
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Score

# Setup Screen
screen = t.Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Instinate Objects
snake = Snake()
food = Food()
score_board = Score()

# Listen For Inputs
screen.listen()
screen.onkeypress(fun = snake.upward, key = "w")
screen.onkeypress(fun = snake.downward, key = "s")
screen.onkeypress(fun = snake.left, key = "a")
screen.onkeypress(fun = snake.right, key = "d")

# Game Loop
game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    sleep(0.04)

    # Collision with Tail
    if snake.check_collision():
        score_board.reset()
        snake.reset()

    if snake.head.xcor() > 278 or snake.head.xcor() < -278 or snake.head.ycor() > 278 or snake.head.ycor() < -278:
        score_board.reset()
        snake.reset()

    # Colision with Food
    for pos in snake.get_position():
        if food.distance(pos) < 20:
            food.refresh()
            score_board.increase_score()
            score_board.update_score()

            snake.segments.append(snake.create_segment(snake.new_pos))
            snake.new_cord_value - 20


# Close on Click
screen.exitonclick()