from random import randint
from tkinter import *
from tkinter import ttk, messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Character pools for password generation
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    """Generates a random password and inserts it into the password entry field."""
    password_entry.delete(0, END)
    password_letter = [random.choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Automatically copy the password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    """Saves website, email, and password to a JSON file."""
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_password():
    """Looks up and displays saved login credentials for a given website."""
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="You haven't stored any passwords yet")
    else:
        if website in data:
            messagebox.showinfo(
                title=f"{website} details",
                message=f"Your email: {data[website]['email']}\nYour password: {data[website]['password']}"
            )
        else:
            messagebox.showinfo(
                title="No such website exists",
                message="There is no password stored for this website"
            )

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

# Logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website entry
website_label = Label(text="Website:", font=("Arial", 10), fg="black", bg="white")
website_label.grid(column=0, row=1)
website_entry = ttk.Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Email entry
email_label = Label(text="Email/Username:", font=("Arial", 10), fg="black", bg="white")
email_label.grid(column=0, row=2)
email_entry = ttk.Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)

# Password entry
password_label = Label(text="Password:", font=("Arial", 10), fg="black", bg="white")
password_label.grid(column=0, row=3)
password_entry = ttk.Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass_button = ttk.Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = ttk.Button(text="Add", width=50, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = ttk.Button(text="Search", width=16, command=search_password)
search_button.grid(column=2, row=1)

# Run the app
window.mainloop()