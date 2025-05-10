from turtle import Turtle               # Import the Turtle class
import random                           # Import the random module

class Food(Turtle):                     # Creating the Food class and inheriting turtle class
    def __init__(self):
        super().__init__()              # Initialising methods from Turtle class
        self.shape("circle")            # Setting the shape of the food to circle
        self.penup()                    # Pulling the penup so it doesn't draw
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)            # Decreasing the size fo the food
        self.color("blue")              # Setting the color of Food
        self.speed("fastest")           # Displaying it with the fastest speed so that the user doesn't see the animation
        self.refresh()                  # calling the refresh()

    def refresh(self):                                    # Creating refresh() to refresh the food position after it's eaten
        random_x = random.randint(-280, 280)           # Generating random xcor
        random_y = random.randint(-280, 280)           # Generating random ycor
        self.goto(random_x, random_y)                     # Setting the position of the food based on random coordinates
