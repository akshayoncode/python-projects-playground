from turtle import Turtle                           # Importing the turtle library

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]    # Defining starting positions as constant so that we only have to change at one place in the future
MOVE_DISTANCE = 20                                  # Defining the snake movement as constant
UP = 90                                             # Defining the headings as constant
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:                                        # Creating the Snake class
    def __init__(self):
        self.segments = []                          # Creating an empty list for snake head and body squares
        self.create_snake()                         # Triggering the create_snake() whenever this class is called
        self.head = self.segments[0]                # Setting the head position for the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:         # Creating the snake head and body and sending it to position using add_segment()
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")        # Setting the snake shape
        new_segment.color("white")                  # Setting the snake color
        new_segment.penup()                         # Pulling the pen up
        new_segment.shapesize(stretch_len=0.9, stretch_wid=0.9)
        new_segment.goto(position)                  # Sending the snake to the required position
        self.segments.append(new_segment)           # Appending the snake to the self.segments[]

    def extend(self):                                             # Creating extend() to extend the length of snake
        self.add_segment(self.segments[-1].position())            # Adding a segment to the end of the snake's tail

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):    # Updating the position of squares from the end of the body
            new_x = self.segments[seg_num - 1].xcor()           # Storing the x-cor of the square ahead
            new_y = self.segments[seg_num - 1].ycor()           # Storing the y-cor of the square ahead
            self.segments[seg_num].goto(new_x, new_y)           # Moving the position of a square to the square ahead
        self.head.forward(MOVE_DISTANCE)                        # Moving the head by MOVE_DISTANCE steps

    def up(self):
        if self.head.heading() != DOWN:              # Checking that the head is not pointing Down
            self.head.setheading(UP)                 # Making the head of snake point UP = 90

    def down(self):
        if self.head.heading() != UP:                # Checking that the head is not pointing Up
            self.head.setheading(DOWN)               # Making the head of snake point DOWN = 90

    def left(self):
        if self.head.heading() != RIGHT:             # Checking that the head is not pointing RIGHT
            self.head.setheading(LEFT)               # Making the head of snake point LEFT = 90

    def right(self):
        if self.head.heading() != LEFT:              # Making the head of snake point LEFT = 90
            self.head.setheading(RIGHT)              # Making the head of snake point RIGHT = 90
