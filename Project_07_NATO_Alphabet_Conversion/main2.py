import pandas

# Load the NATO phonetic alphabet CSV into a DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping each letter to its NATO phonetic code
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Function to convert user input into a list of NATO phonetic codes
def nato_convert():
    user_input = input("What is the word: ").upper()  # Get user input and convert to uppercase
    try:
        # Convert each letter to its corresponding NATO code
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        # If input contains non-alphabet characters, show error and retry
        print("Only letters in the alphabet please.")
        nato_convert()
    else:
        # If successful, print the list of phonetic codes
        print(nato_list)

# Run the converter
nato_convert()