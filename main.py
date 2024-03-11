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

def main():
    game_is_on = True
    score = 0

    while game_is_on:
        snake.move()
        screen.update()
        sleep(0.04)

        if snake.check_collision():
            return None

        for pos in snake.get_position():
            if food.distance(pos) < 20:
                food.refresh()
                score += 1
                score_board.write_score(score)
                
                snake.segments.append(snake.create_segment(snake.new_pos))
                snake.new_cord_value - 20

        
main()

# Close on Click
screen.exitonclick()