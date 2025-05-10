import random                                       # Import random library to generate a random word to guess
import hangman_words                                # Import the file containing list of words
import hangman_art                                  # Import the file containing Hangman logo and stages in ASCII

word_list = hangman_words.word_list                 # Saving the word list in the program
lives = 6                                           # Defining number of lives for the user
stages = hangman_art.stages                         # Saving the Hangman stages art
print(hangman_art.logo)                             # Printing the logo

chosen_word = random.choice(word_list)              # Choosing a random word for the user to guess
placeholder = ""                                    # Creating an empty placeholder string to show to user later
word_length = len(chosen_word)
for position in range(word_length):                 # Filling placeholder text with dashes equal to the number of letters in the word
    placeholder += "_"
print("Word to guess: " + placeholder)              # Printing the placeholder containing _

game_over = False                                   # Setting the flag for while loop
correct_letters = []                                # Creating an empty list to track the guessed letters

while not game_over:                                # Continue the game until not over
    print(f"****************************{lives}/6 LIVES LEFT****************************")   # Showing the remaining lives to the user
    guess = input("Guess a letter: ").lower()        # Asking the user to guess a letter

    if guess in correct_letters:                     # prompt the user if they have guessed the letter already
        print("You already guessed this letter")

    display = ""                                     # Create an empty string to concatenate the letters guessed

    for letter in chosen_word:                       # Loop through each letter against the guess
        if letter == guess:                          # If guessed letter matches the letter in the word
            display += letter                        # Add the guessed letter to display
            if letter not in correct_letters:        # If guessed letter is not in the letters guessed already
                correct_letters.append(guess)        # Append the letter to correct_letters list
        elif letter in correct_letters:              # If guessed letter has been guessed before
            display += letter                        # Add that letter to display
        else:                                        # If the guessed letter is not in the word
            display += "_"                           # Add _ to display

    print("Word to guess: " + display)               # Show the updated letters after each guess to the user

    if guess not in chosen_word:                     # Deduct a life if the guessed letter is not in the word
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:                               # Set the game_over flag to True if lives = 0
            game_over = True
            print(f"***********************YOU LOSE**********************\n"
                  f"The word was {chosen_word}")     # Print the word, and show game lost message

    if "_" not in display:                           # Check if there are no _ in display which means that user guessed the word
        game_over = True                             # Set the game_over flag to True since user guessed the word
        print("****************************YOU WIN****************************")

    print(stages[lives])                             # Print respective stages art based on remaining lives
