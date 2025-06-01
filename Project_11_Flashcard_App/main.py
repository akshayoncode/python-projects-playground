from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}       # Will hold list of word dictionaries
current_card = {}    # Holds the currently displayed word pair

# ---------------------------- DATA LOADING ---------------------------- #
# Try to load saved progress; fallback to original word list
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# -------------------------- GENERATING WORDS -------------------------- #
def print_card():
    """Display a new French word and schedule flip to English after 3 seconds."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel previous flip
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_background, image=front_img)
    canvas.itemconfig(front_lang_title, text="French", fill="black")
    canvas.itemconfig(front_lang_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """Flip the card to show the English translation."""
    canvas.itemconfig(card_background, image=back_img)
    canvas.itemconfig(front_lang_title, text="English", fill="white")
    canvas.itemconfig(front_lang_word, text=current_card["English"], fill="white")

# -------------------------- SAVING KNOWN WORDS ------------------------ #
def is_known():
    global current_card
    """Remove known word from data and update the CSV."""
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    print_card()  # Show the next card

# -------------------------- UI SETUP ---------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

# Start flip timer
flip_timer = window.after(3000, func=flip_card)

# Flashcard canvas
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 280, image=front_img)
front_lang_title = canvas.create_text(400, 180, text="", font=("Arial", 24, "italic"))
front_lang_word = canvas.create_text(400, 270, text="", font=("Arial", 32, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons for user input
wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, border=0, highlightthickness=0, command=print_card)
button_wrong.grid(column=0, row=2)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, border=0, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=2)

# Show the first card
print_card()

# Run the application
window.mainloop()