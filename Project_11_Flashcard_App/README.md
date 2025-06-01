# Project 11: Flashcard App (French to English)

## Project Summary

This project is an interactive flashcard app built using Python’s `tkinter` and `pandas` libraries. It helps users learn French vocabulary by displaying a random French word and flipping the card to show its English translation after a few seconds. Users can mark words they know, which are then removed from future practice sessions and saved for progress tracking.

This project was built as part of my ongoing Python learning journey to enhance my skills in GUI development, data persistence, and interactive educational tools.

## Features

- Displays French words and flips to English after a delay
- Tracks user progress and removes known words from future sessions
- Automatically saves learning progress to a CSV file
- Clean and visually engaging GUI using flashcard-style images
- Buttons to mark words as known or unknown

## How to Run

Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.

### Steps:

1. Download or clone this repository.
2. Navigate to the project folder in your terminal:
   cd Project_11_Flashcard_App
3. python3 main.py

## Controls
1. ✅ Right button: Mark the current word as known and move to the next
2. ❌ Wrong button: Skip and move to the next word without saving progress

## What I learned
1. Using pandas to read and update structured CSV data
2. Implementing timed events with tkinter using after() and after_cancel()
3. Dynamically updating canvas elements with changing content and images
4. Structuring learning tools with persistent progress tracking
5. Building visually engaging, user-friendly GUI applications

## Files
1. main.py – Flashcard app logic and UI
2. data/french_words.csv – Full list of French-English vocabulary
3. data/words_to_learn.csv – Saved progress; updated after each known word
4. images/card_front.png – Front of the flashcard (French side)
5. images/card_back.png – Back of the flashcard (English side)
6. images/right.png – Button to mark word as known
7. images/wrong.png – Button to mark word as unknown

## Future Improvements
1. Add language selection (e.g., Spanish, German, etc.)
2. Include text-to-speech for pronunciation assistance
3. Show learning stats like words learned or success rate
4. Add user profiles to support multiple learners