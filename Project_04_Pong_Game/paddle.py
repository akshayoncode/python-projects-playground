from turtle import Turtle                       # Importing the turtle library

class Paddle(Turtle):                           # Creating the Paddle class and inheriting turtle class
    def __init__(self, x_pos, y_pos):           # Initialising the class and passing x and y coordinates for each paddle
        super().__init__()                      # Initialising the Super Class
        self.shape("square")                    # Setting the paddle attributes
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x_pos, y_pos)                 # Sending the paddle to the passed coordinates

    def up(self):                               # Creating a method to move the paddle up upon key press
        new_y = self.ycor() + 30                # Moving the paddle 30 steps up
        self.goto(self.xcor(), new_y)

    def down(self):                             # Creating a method to move the paddle up upon key press
        new_y = self.ycor() - 30                # Moving the paddle 30 steps down
        self.goto(self.xcor(), new_y)
