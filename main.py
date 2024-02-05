from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ping pong game")
screen.listen()

screen.tracer(0)

player1 = Paddle(350, 0)
player2 = Paddle(-350, 0)



ball = Ball()

screen.onkeypress(player1.move_up, "Up")
screen.onkeypress(player1.move_down, "Down")

screen.onkeypress(player2.move_up, "w")
screen.onkeypress(player2.move_down, "s")

game_is_on = True
score = Scoreboard()
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.01)        #delay with 0.01s, so we can see the ball move

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # colloision with paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounceWall()

    elif ball.xcor() > 350:
        ball.reset_position()
        score.player2Score()

    elif ball.xcor() < -350:
        ball.reset_position()
        score.player1Score()


screen.exitonclick()

