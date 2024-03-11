from turtle import Turtle
FONT = ("Courier",16,"bold")
ALLIGN = ("center")
POSITION = 0, 270

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(POSITION)

    def write_score(self,score):
        self.clear()
        self.write(arg = f"Score: {score}", align= ALLIGN, font= FONT)

    def write_game_over(self, score):
        self.clear()
        self.goto(0,0)
        self.write(arg = f"Game Over. You Got {score} Apples.", align= ALLIGN, font= FONT)
        