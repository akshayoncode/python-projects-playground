from turtle import Turtle
import random

# Predefined car colors and movement configuration
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Initial car speed
MOVE_INCREMENT = 5  # Speed increase per level


class CarManager:
    """Manages the generation, movement, and speed of cars in the game."""

    def __init__(self):
        self.all_cars = []  # List to keep track of all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Current speed of cars

    def generate_car(self):
        """Randomly generate a new car and add it to the screen."""
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a new car
            new_car.penup()  # Prevent drawing lines
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make the car rectangular
            new_car.color(random.choice(COLORS))  # Assign random color
            random_y = random.randint(-200, 250)  # Random vertical position
            new_car.goto(300, random_y)  # Start from the right edge
            self.all_cars.append(new_car)  # Add to the car list

    def move_cars(self):
        """Move all existing cars to the left."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase the speed of all cars for the next level."""
        self.car_speed += MOVE_INCREMENT