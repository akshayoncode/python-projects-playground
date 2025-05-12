import time                                      # Importing the Libraries and Classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()                                # Creating the screen object
screen.setup(width=800, height=600)              # Setting screen attributes
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)                                 # Turning the animation off
r_paddle = Paddle(375, 0)           # Sending right paddle to the right portion of the screen
l_paddle = Paddle(-375, 0)                # Sending left paddle to the left portion of the screen
ball = Ball()                                   # Creating the ball object
scoreboard = Scoreboard()                       # Creating the scoreboard object

screen.listen()                                 # Start listening to the keystrokes
screen.onkey(r_paddle.up, "Up")            # Controlling the right paddle with up and down arrow keys
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")             # Controlling the left paddle with W and S keys
screen.onkey(l_paddle.down, "s")

game_on = True                                        # Setting a flag to keep the game running
while game_on:
    time.sleep(ball.move_speed)                       # Set a delay to the ball's animation
    screen.update()                                   # Update the screen after the animation is performed
    ball.move()                                       # Start moving the ball
    if ball.ycor() > 280 or ball.ycor() < -280:       # Checking if the ball touches the topmost or the bottom area of the screen
        ball.bounce_y()                               # Bounce the ball in the opposite y-cor direction

    # Checking if the ball touches the left or right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()                               # Bounce the ball in the opposite x-cor direction

    if ball.xcor() > 400:                             # Checking if the ball misses the right paddle
        ball.ball_reset()                             # Reset the ball
        scoreboard.l_point()                          # Give one point to the left paddle

    if ball.xcor() < -400:                            # Checking if the ball misses the left paddle
        ball.ball_reset()                             # Reset the ball
        scoreboard.r_point()                          # Give one point to the right paddle

screen.exitonclick()
