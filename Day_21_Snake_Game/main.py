from turtle import Screen     # Importing the Libraries and Classes
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()                     # Creating the screen
screen.setup(width=600, height=600)   # Setting screen dimensions
screen.bgcolor("black")               # Setting the screen background
screen.title("Snake Game")            # Setting the title of the game
screen.tracer(0)                      # Turns the animation off

snake = Snake()                       # Creating the snake object
food = Food()
score_board = Scoreboard()
screen.listen()                       # Setting the screen to listen to events
screen.onkey(snake.up, "Up")     # Calling up() of the Snake class to move snake up on Up arrow key
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True                     # Setting a flag to keep the game running
while game_is_on:
    screen.update()                   # Update the screen after the animation is performed
    time.sleep(0.1)                   # With a delay of 0.1 seconds
    snake.move()                      # Calling move() of the Snake class to move the snake automatically

    if snake.head.distance(food) < 18:     # Detect Collision with food
        food.refresh()                     # Refresh the screen with new food
        snake.extend()                     # Extend the body fo the snake
        score_board.increase_score()       # Increase score by 1

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False                 # Set the game over flag
        score_board.game_over()            # Show the final score to the user

    for segment in snake.segments[1:]:               # Detect collision with tail
        if snake.head.distance(segment) < 10:        # Check whether the head of snake if too near to the tail
            game_is_on = False                       # Set the game over flag
            score_board.game_over()                  # Show the final score to the user

screen.exitonclick()