import turtle as t
import random

class Food():
    def __init__(self, screen_width, screen_height, snake_pos) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_pos = snake_pos
        self.x_bound = (self.screen_width // 2) - 20
        self.y_bound = (self.screen_height // 2) - 20

    def create_food(self):
        self.food = t.Turtle("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(random.randint(-self.x_bound, self.x_bound), 
                       random.randint(-self.y_bound, self.y_bound))
    
    def check_collision(self):
        score = 0 
        if self.food.pos() in self.snake_pos:
            self.food.reset()
            self.create_food()
            score += 1
            print(f"{score=}")