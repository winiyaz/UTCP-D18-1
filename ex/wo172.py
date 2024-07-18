from turtle import Turtle, Screen
import random as rp

# Turtle setup ---
to = Turtle()  # Initialize Turtle Class
to.sc = Screen()  # Initialize Screen Class

# Turtle graphics initialize
def to_init():
    to.color("coral")  # Setting color
    to.sc.register_shape("ax.gif")  # Register/ Initialize Shape
    to.shape("ax.gif")  # Use Shape
    to.shapesize(stretch_wid=3, stretch_len=3, outline=1)  # Setting size params
    to.sc.bgcolor("#020617")  # Set Bg Color

to_init()

# Main Here

# Setting The color - taken from https://trinket.io/docs/colors
colo = [
    "lime",
    "deep pink",
    "deep sky blue",
    "yellow",
    "magenta",
    "lavender blush"
]

# Robot movement

directions = [0, 90, 180, 270]  # Directions
to.speed("fastest")

for _ in range(200):
    to.forward(100)
    to.setheading(rp.choice(directions))
    to.color(rp.choice(colo))
    to.pensize(rp.randint(1, 10))

# --- Exiting on click function
to.sc.exitonclick()