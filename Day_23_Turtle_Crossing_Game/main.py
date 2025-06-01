from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

# --- Setup screen ---
screen = Screen()
screen.setup(width=600, height=600)     # Set the window size
screen.bgcolor("white")                 # Background color
screen.title("Turtle Crossing Game")    # Window title
screen.tracer(0)                        # Turn off automatic updates for manual control

# --- Create game objects ---
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# --- Set up keyboard input ---
screen.listen()
screen.onkey(player.move, "space")      # Move player turtle on space key press

# --- Main game loop ---
is_game_on = True
while is_game_on:
    time.sleep(0.1)                     # Pause to control game speed
    screen.update()                     # Refresh the screen

    cars.generate_car()                 # Randomly add new cars
    cars.move_cars()                    # Move all cars across the screen

    # --- Check if player has reached the top (crossed successfully) ---
    if player.ycor() > 280:
        player.reset_turtle()           # Reset turtle to bottom
        cars.level_up()                 # Increase car speed
        scoreboard.increase_level()     # Update level on screen

    # --- Check for collision with any car ---
    for item in cars.all_cars:
        if player.distance(item) < 22:  # Collision threshold
            is_game_on = False
            scoreboard.game_over()      # Display "GAME OVER"

# --- Keep window open after game ends ---
screen.exitonclick()