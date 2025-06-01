from turtle import Turtle

# Constants for the font style and text alignment
FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    """Handles the game level display and game over message."""

    def __init__(self):
        super().__init__()
        self.level = 1                    # Initial level
        self.color("black")              # Text color
        self.penup()
        self.hideturtle()                # Hide the turtle shape; only show text
        self.goto(-240, 270)             # Position the scoreboard on top-left
        self.update_scoreboard()

    def update_scoreboard(self):
        """Display the current level on the screen."""
        self.write(f"Level {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """Increase the level by 1 and update the display."""
        self.level += 1
        self.clear()                     # Clear the previous level text
        self.update_scoreboard()

    def game_over(self):
        """Display 'GAME OVER' in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)