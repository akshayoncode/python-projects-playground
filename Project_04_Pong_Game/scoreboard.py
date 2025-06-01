from turtle import Turtle                             # Importing the turtle library

class Scoreboard(Turtle):                             # Creating the Ball class and inheriting turtle class
    def __init__(self):                               # Initialising the class
        super().__init__()                            # Initialising the Super class
        self.color("white")                           # Setting the scoreboard attributes
        self.penup()
        self.hideturtle()
        self.l_score = 0                              # Creating flags to track the score
        self.r_score = 0
        self.update_score()

    def update_score(self):                            # Creating a method to update and display the score
        self.clear()                                   # Clearing the previous score
        self.goto(-100, 200)                        # Moving score to the top of the screen
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))         # Print the score of the left paddle
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))         # Print the score of the right paddle

    def l_point(self):                                 # Method to increment the score for the left paddle
        self.l_score += 1
        self.update_score()

    def r_point(self):                                 # Method to increment the score for the left paddle
        self.r_score += 1
        self.update_score()
