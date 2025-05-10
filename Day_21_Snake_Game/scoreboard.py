from turtle import Turtle                    # Import the Turtle class
ALIGNMENT = "center"                         # Setting the alignment of scoreboard as constant
FONT = ("Arial", 16, "normal")               # Setting the font of scoreboard as constant

class Scoreboard(Turtle):                    # Creating Scoreboard class and inheriting Turtle class
    def __init__(self):
        super().__init__()                   # Initialising methods from Turtle class
        self.score = 0                       # Initialising with score = 0
        self.color("white")                  # Setting the color of the scoreboard
        self.hideturtle()                    # Hiding the Turtle shape
        self.penup()                         # Pulling the penup so it doesn't draw
        self.goto(0, 270)              # Sending the scoreboard to the top of the screen
        self.update_scoreboard()             # Calling the update_scoreboard method

    def update_scoreboard(self):             # Creating update_scoreboard method to display the scoreboard
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)          # Using the write() method from Turtle to display the score

    def increase_score(self):                # Creating increase_score method to update the score when food gets eaten
        self.score += 1                      # Incrementing the score by 1
        self.clear()                         # Clearing the previous score
        self.update_scoreboard()             # Displaying the updated score using update_score method

    def game_over(self):                     # Creating the game over sequence
        self.goto(0,0)                 # Setting position to the middle of the screen
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)     # Displaying game over text
