from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-180, 180)
        self.write(self.player2_score, align="center", font=("Courier", 80, "normal"))

        self.goto(180, 180)
        self.write(self.player1_score, align="center", font=("Courier", 80, "normal"))

    def player1Score(self):
        self.player1_score += 1
        self.updateScore()

    def player2Score(self):
        self.player2_score += 1
        self.updateScore()