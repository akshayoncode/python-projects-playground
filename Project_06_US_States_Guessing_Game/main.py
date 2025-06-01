import turtle
import pandas as pd

# Load the CSV file containing state names and coordinates
data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()  # Convert state column to a list

# Set up the screen with a U.S. map image
screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Initialize game variables
guessed_states = []
screen.tracer(0)  # Prevent automatic screen updates (optional performance improvement)
is_game_on = True

# Main game loop: continue until 50 states are guessed
while len(guessed_states) < 50:
    # Prompt the user to guess a state
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 guessed",
        prompt="What's another state's name?"
    ).title()  # Convert input to Title Case (e.g., 'texas' -> 'Texas')

    # Allow user to exit the game and generate a learning file
    if answer_state == "Exit":
        missed_states = [state for state in state_list if state not in guessed_states]
        data_frame = pd.DataFrame(missed_states)
        data_frame.to_csv("states_to_learn.csv")  # Save unguessed states to a CSV file
        break

    # If the guessed state is correct and hasn't been guessed yet
    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Create a new turtle to write the state name on the map
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]  # Get row matching the guessed state
        t.goto(state_data.x.item(), state_data.y.item())  # Move to the state's coordinates
        t.write(answer_state)  # Display the state's name on the map