# Project 06: U.S. States Guessing Game

## Project Summary

This project is a U.S. geography quiz game built using Python's turtle graphics module and pandas. The player is shown a blank map of the United States and must correctly name all 50 states. As the user guesses correctly, the state's name appears on the map at its corresponding location.

This project was built as part of my ongoing Python learning journey to strengthen my skills in file handling, event-driven programming, and data manipulation with pandas.

## Features

- Interactive U.S. map using turtle graphics
- Real-time user input with validation
- Displays guessed state names directly on the map
- Tracks and stores missed states in a CSV for further learning
- Smooth integration of data from external CSV files

## How to Run

Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.

### Steps:

1. Download or clone this repository.
2. Navigate to the project folder in your terminal:
   cd Project_06_US_States_Game
3. python3 main.py

## Controls
1. Type the name of a U.S. state in the prompt window.
2. Capitalization is automatically corrected.
3. Type Exit to end the game early and generate a learning file.

## What I learned
1. How to use turtle graphics to create custom graphical interfaces
2. Handling user input in real time with textinput()
3. Reading and filtering data using pandas DataFrames
4. Writing dynamic text to the screen based on user input
5. Generating new CSV files based on game state (missed states)

## Files
1. main.py – Game logic and user interface
2. 50_states.csv – Data source for state names and coordinates
3. blank_states_img.gif – U.S. map used as background

## Future Improvements
1. Add a timer to make the game more challenging
2. Include hints or region-based grouping (e.g., “East Coast”)
3. Implement scoring and a leaderboard
4. Add sounds or animations when states are guessed correctly