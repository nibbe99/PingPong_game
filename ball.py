from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 4
        self.y_move = 4

    def move(self):
        self.penup()
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move = -self.y_move

    def bounceWall(self):
        self.x_move = -self.x_move

    def reset_position(self):
        self.goto(0,0)
        self.bounceWall()