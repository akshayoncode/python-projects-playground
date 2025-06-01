from tkinter import *

# Function to convert miles to kilometers when button is clicked
def calculate():
    input_value = input.get()                          # Get the value from the Entry field
    km_value = round(float(input_value) * 1.6, 2)      # Convert miles to km and round to 2 decimal places
    converted_label = Label(text=km_value, font=("Arial", 12))  # Create a new label with the result
    converted_label.grid(column=3, row=4)              # Place the result in the UI grid

# Create the main window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)                       # Add padding around the window

# Entry widget for user input (number of miles)
input = Entry(width=10, font=("Arial", 12))
input.grid(column=3, row=3)

# Static label showing "Miles"
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=4, row=3)

# Label showing "is equal to"
equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=4)

# Static label showing "Km"
km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=4, row=4)

# Button to trigger the conversion
cal_button = Button(text="Calculate", font=("Arial", 12), command=calculate)
cal_button.grid(column=3, row=5)

# Keep the window running
window.mainloop()