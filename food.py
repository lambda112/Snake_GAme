from turtle import Turtle
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Food(Turtle): 
    def __init__(self) -> None:
        super().__init__()
        self.screen_width = SCREEN_WIDTH // 2
        self.screen_height = SCREEN_HEIGHT // 2

        self.color("red")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)

    def refresh(self):
        x_bound = [num for num in range(0, self.screen_width - 1) if num % 20 == 0]
        y_bound = [num for num in range(0, self.screen_height - 1) if num % 20 == 0]
        x_val = (-random.choice(x_bound), random.choice(x_bound))
        y_val = (-random.choice(y_bound), random.choice(y_bound))
        self.goto(random.randint(x_val[0], x_val[1]),random.randint(y_val[0], y_val[1]))
