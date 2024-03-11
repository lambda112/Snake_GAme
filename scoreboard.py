from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(x= 0, y=270)

    def write_score(self,score):
        self.clear()
        self.write(arg = f"Score: {score}", align= "center",font=("Arial",16,"normal"))
        