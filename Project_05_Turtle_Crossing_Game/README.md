# Project 05: Turtle Crossing Game

## Project Summary

This project is a recreation of the classic Frogger-style crossing game using Python's turtle graphics module. A player-controlled turtle moves upward across the screen, dodging cars that spawn at random positions and speeds. The game includes collision detection, level tracking, and smooth motion updates using the `turtle` and `time` modules.

This project was built as part of my ongoing Python learning journey to strengthen my skills in object-oriented programming and event-driven development.

## Features

- Player-controlled turtle with smooth movement
- Random car generation in different colours
- Level system with increasing difficulty
- Real-time collision detection and Game Over message
- Clean modular structure using classes and multiple files

## How to Run

Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.

### Steps:

1. Download or clone this repository.
2. Navigate to the project folder in your terminal:
   cd Day_23_Turtle_Crossing_Game
3. python3 main.py

## Controls
1. Press the Spacebar to move the turtle upward.

## What I learned
1. How to use the turtle module to animate movement and build graphical applications
2. Working with keyboard input and event listeners
3. Structuring a Python program using classes across multiple files
4. Using randomization to simulate dynamic game elements
5. Handling collisions and screen updates for smoother gameplay

## Files
1. main.py – Game loop and screen setup
2. player.py – Player turtle logic and movement
3. car_manager.py – Car creation, motion, and level progression
4. scoreboard.py – Display and update of game level and Game Over message

## Future Improvements
1. Add a start screen with instructions
2. Implement sound effects for collision and level-up events
3. Add lives or health system instead of instant game over
4. Create varying obstacle types or patterns for added difficulty