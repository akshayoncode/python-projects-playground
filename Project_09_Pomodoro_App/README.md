# Project 09: Pomodoro App

## Project Summary

This project is a GUI-based Pomodoro timer built using Python’s `tkinter` module. It implements the Pomodoro Technique — a time management method that uses work sessions and short breaks to boost productivity. The timer automatically cycles through work periods, short breaks, and long breaks with visual indicators and session tracking.

This project was built as part of my ongoing Python learning journey to practice GUI development, time-based event handling, and user interface logic.

## Features

- Fully functional Pomodoro timer with automatic session transitions
- Visual checkmarks for each completed work session
- Start and reset buttons to control the timer
- Clear visual feedback using colored labels and a tomato image
- Built using a clean, structured `tkinter` grid layout

## How to Run

Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.

### Steps:

1. Download or clone this repository.
2. Navigate to the project folder in your terminal:
   cd Project_09_Pomodoro_App
3. python3 main.py

## Controls
1. Start: Begins the Pomodoro session and cycles through work/break intervals
2. Reset: Stops the timer and resets everything to the initial state

## What I learned
1. How to build structured GUIs with tkinter
2. Using after() and after_cancel() to manage time-based events
3. Switching UI elements dynamically based on app state
4. Implementing recursive countdown logic in a GUI environment
5. Managing global state across multiple timer sessions

## Files
1. main.py – Full program with logic for the timer, GUI, and control flow
2. tomato.png – Visual centerpiece for the timer canvas (image of a tomato)

## Future Improvements
1. Add sound effects or notifications when sessions end
2. Allow customization of work/break durations via user input
3. Display completed Pomodoros as a session log
4. Minimize to system tray and run in background