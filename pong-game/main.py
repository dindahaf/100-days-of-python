from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


paddle1_score = 0
paddle2_score = 0
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the y wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time.sleep(0)

    # Detect right paddles misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Detect left paddles misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()






screen.exitonclick()