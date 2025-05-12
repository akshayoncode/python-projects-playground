from turtle import Turtle                          # Importing the turtle library

class Ball(Turtle):                                # Creating the Ball class and inheriting turtle class
    def __init__(self):                            # Initialising the class
        super().__init__()                         # Initialising the Super class
        self.shape("circle")                       # Setting the ball attributes
        self.color("white")
        self.penup()
        self.x_pos = 10                            # Creating constant coordinates to control the direction of the ball
        self.y_pos = 10
        self.move_speed = 0.1                      # Creating an attribute to control the speed of the ball

    def move(self):                                # Method to move the ball
        new_x = self.xcor() + self.x_pos           # Moving the ball by 10 steps to the x-cor
        new_y = self.ycor() + self.y_pos           # Moving the ball by 10 steps to the y-cor
        self.goto(new_x, new_y)

    def bounce_y(self):                            # Creating a method to bounce the ball upon hitting the walls
        self.y_pos *= -1                           # Only decreasing y-cor and let x-cor increment

    def bounce_x(self):                            # Creating a method to bounce the ball upon hitting the paddles
        self.x_pos *= -1                           # Reverse the direction by decreasing x-cor
        self.move_speed *= 0.9                     # Speeding up the ball everytime it hits a paddle

    def ball_reset(self):                          # Creating a method to reset the ball upon missing the paddles
        self.goto(0,0)                       # Sending the ball to the center of the screen
        self.move_speed = 0.1                      # Resetting the speed of the ball
        self.bounce_x()                            # Make it go the opposite direction
