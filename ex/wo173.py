# Lesson 172. This one is for setting random colors

import random as rp
from turtle import Turtle, Screen

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
# colo = [
# 	"lime",
# 	"deep pink",
# 	"deep sky blue",
# 	"yellow",
# 	"magenta",
# 	"lavender blush"
# ]

# Robot movement

directions = [0, 90, 180, 270]  # Directions
to.speed("fastest")

# Randomizing colors
to.sc.colormode(255)

def rando_colo():
	"""Random Color generator"""
	r = rp.randint(0,255)
	g = rp.randint(0,255)
	b = rp.randint(0,255)
	ra_co = (r,g,b)
	return ra_co


for _ in range(200):
	to.forward(30)
	to.backward(20)
	to.setheading(rp.choice(directions))
	to.color(rando_colo())
	to.pensize(rp.randint(5, 15))

# --- Exiting on click function
to.sc.exitonclick()
