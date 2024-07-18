# this is th turtle graphics initalizer
# Work from 171
import random as rp
from turtle import Turtle, Screen

# Turtle setup ---

to = Turtle()  # Intitialize Turtle Class
to.sc = Screen()  # Initialize Screen Class


def to_init():
	to.color("coral")  # Setting color
	to.sc.register_shape("ax.gif")  # Register/ Initialize Shape
	to.shape("ax.gif")  # Use Shape
	to.shapesize(stretch_wid=3, stretch_len=3, outline=1)  # Setting size params
	to.sc.bgcolor("#020617")  # Set Bg Color


# Intialize the function
to_init()