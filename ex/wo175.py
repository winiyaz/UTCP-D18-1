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

# --- Exiting on click function
to.sc.exitonclick()

colo_list = [[(31, 35, 68), (73, 82, 139), (121, 74, 104), (48, 50, 104), (59, 33, 54), (185, 130, 161), (90, 46, 76), (162, 104, 139), (227, 142, 94), (140, 80, 62), (114, 105, 169), (195, 96, 79), (114, 150, 196), (65, 41, 32), (32, 53, 40), (102, 47, 40), (66, 104, 82), (232, 161, 190), (84, 169, 74), (41, 81, 53), (74, 81, 29), (23, 80, 97), (40, 157, 202), (241, 193, 231), (122, 174, 141), (236, 169, 157), (247, 193, 118), (194, 208, 236), (250, 202, 157), (162, 130, 79)]
] # This is extracted from img/colo.py using colorgram

print(colo_list)

