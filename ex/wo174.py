# Lesson 174 - Spirograph

import random as rp
from turtle import Turtle, Screen  # Importing the tutle and screen library

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


to_init()  # Initialize the turtle
to.sc.colormode(255)  # Needed for setting the color


def rando_colo():
	"""Random Color generator"""
	r = rp.randint(0, 255)
	g = rp.randint(0, 255)
	b = rp.randint(0, 255)
	ra_co = (r, g, b)
	return ra_co


to.speed("fastest")  # Set speed to fastest

def dr_sp(gap):
	"""Stop the circle animation once it hits 360"""
	for _ in range(int(360 / gap)):
		to.color(rando_colo())
		to.circle(150)
		to.setheading(to.heading() + gap)
		to.pensize(rp.randint(1, 15))

# call above function
dr_sp(100)


# --- Exiting on click function
to.sc.exitonclick()
