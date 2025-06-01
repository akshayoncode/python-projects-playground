# Project 07: NATO Phonetic Alphabet Converter

## Project Summary

This project is a command-line tool that converts any word into its equivalent NATO phonetic alphabet code using data from a CSV file. Each letter in the input word is mapped to its corresponding NATO code (e.g., "A" becomes "Alpha", "B" becomes "Bravo", etc.).

This project was built as part of my ongoing Python learning journey to improve my skills in reading data files, working with dictionaries, and handling user input with error checking.

## Features

- Converts any alphabetical word into NATO phonetic codes
- Uses a CSV file to dynamically build the letter-to-code mapping
- Automatically handles both uppercase and lowercase user input
- Recursively re-prompts the user on invalid input (non-letters)
- Clean output in list format

## How to Run

Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.

### Steps:

1. Download or clone this repository.
2. Navigate to the project folder in your terminal:
   cd Project_07_NATO_Phonetic_Converter
3. python3 main2.py

## Controls
1. Enter a word (e.g., hello) when prompted.
2. Output will be a list of corresponding NATO phonetic codes.
3. Type letters only — the script will re-prompt if invalid input is entered.

## What I learned
1. How to read and iterate over CSV data using pandas
2. Creating dictionaries dynamically with dictionary comprehensions
3. Validating user input and handling exceptions
4. Structuring a command-line program with clear output and logic
5. Using recursion to handle input retry patterns

## Files
1. main.py – Core logic for conversion and user interaction
2. nato_phonetic_alphabet.csv – CSV file mapping each letter to its NATO phonetic code

## Future Improvements
1. Add GUI support using Tkinter
2. Allow saving the output to a text file
3. Support multiple word inputs or full sentences