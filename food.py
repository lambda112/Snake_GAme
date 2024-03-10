import turtle as t
import random

class Food(): 
    def __init__(self, screen_width, screen_height) -> None:
        self.screen_width = screen_width // 2
        self.screen_height = screen_height // 2
        self.score = 0
        self.food = t.Turtle("circle")
        self.x_bound = [num for num in range(0, self.screen_width - 1) if num % 20 == 0]
        self.y_bound = [num for num in range(0, self.screen_height - 1) if num % 20 == 0]

    def create_food(self):
        self.food.color("red")
        self.food.penup()
        x_val = (-random.choice(self.x_bound), random.choice(self.x_bound))
        y_val = (-random.choice(self.y_bound), random.choice(self.y_bound))
        self.food.goto(random.randint(x_val[0], x_val[1]),random.randint(y_val[0], y_val[1]))
    
    def check_collision(self, snake_pos):
        for pos in snake_pos:
            if self.food.distance(pos) < 20:
                self.food.clear()
                self.create_food()
                self.score += 1
                print(f"{self.score=}")
                return True
        else:
            return False
        