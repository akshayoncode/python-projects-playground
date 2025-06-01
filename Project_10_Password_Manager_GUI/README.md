# Project 10: Password Manager

## Project Summary

This project is a secure and interactive password manager application built using Python’s `tkinter` module. It allows users to generate strong random passwords, store them locally in a JSON file, and retrieve login credentials for different websites. The interface is designed to be simple, fast, and efficient for everyday password management.

This project was built as part of my ongoing Python learning journey to apply concepts like GUI development, file handling, error checking, and modular programming.

## Features

- Generates strong, random passwords with letters, symbols, and numbers
- Automatically copies generated password to clipboard
- Saves passwords along with website and email/username to a JSON file
- Looks up stored credentials by website name
- Intuitive and responsive GUI built with `tkinter` and `ttk`

## How to Run

Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.

### Steps:

1. Download or clone this repository.
2. Navigate to the project folder in your terminal:
   cd Project_10_Password_Manager
3. python3 main.py

## Controls
1. Website: Enter the name of the website.
2. Email/Username: Enter your login email or username.
3. Click Generate Password to create a secure password.
4. The password is auto-copied to your clipboard.
5. Add: Saves the credentials to data.json.
6. Search: Looks up saved credentials for the entered website.

## What I learned
1. How to build interactive GUI applications using tkinter and ttk
2. Reading from and writing to JSON files
3. Validating and handling user input with messagebox
4. Creating reusable password generators
5. Copying data to the clipboard using pyperclip

## Files
1. main.py – Main program with GUI logic, password generation, and data handling
2. logo.png – Displayed image in the application

## Future Improvements
1. Add master password protection and encryption
2. Create a backup and restore option for the data.json file
3. Add a feature to update or delete stored credentials
4. Allow filtering or listing of all saved websites