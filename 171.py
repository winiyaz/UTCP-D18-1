# Work from 171
import turtle
from turtle import Turtle, Screen
import random as rp

# Turtle setup ---

to = Turtle()  #Intitialize Turtle Class
to.sc = Screen()  # Initialize Screen Class
to.color("coral")  # Setting color
to.sc.register_shape("ax.gif")  # Register/ Initialize Shape
to.shape("ax.gif")  # Use Shape
to.shapesize(stretch_wid=3, stretch_len=3, outline=1) # Setting size params
to.sc.bgcolor("#020617") # Set Bg Color


# Exercise

# Setting The color - taken from https://trinket.io/docs/colors
colo = [
"lime",
"deep pink",
"deep sky blue",
"yellow"
]

def draw_shape(num_sides):
	''' Function for drawing the shape '''
	angle = 360 / num_sides
	for _ in range(num_sides):
		to.forward(100)
		to.right(angle)

for shape_sides_n in range(3,11):
	to.color(rp.choice(colo))
	draw_shape(shape_sides_n)





# --- Exiting on click function
to.sc.exitonclick()
# ---