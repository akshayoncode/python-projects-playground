from turtle import Turtle

# Constants for the player's starting position and how far it moves each time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30


class Player(Turtle):
    """Represents the player (turtle) in the Turtle Crossing game."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Set the shape of the turtle
        self.setheading(90)  # Make the turtle face upwards
        self.penup()  # Prevent drawing when the turtle moves
        self.reset_turtle()  # Place turtle at the starting position
        self.move()  # Make the initial move forward

    def move(self):
        """Move the turtle forward by a fixed distance."""
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        """Reset the turtle back to the starting position."""
        self.goto(STARTING_POSITION)