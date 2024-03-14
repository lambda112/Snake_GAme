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
        self.penup()
        self.score = 0

        with open("high_score.txt", "r") as file:
            self.highscore = file.read()

        self.highscore = int(self.highscore)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg = f"Score: {self.score} High Score: {self.highscore}", align= ALLIGN, font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        