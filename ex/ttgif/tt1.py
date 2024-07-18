import random as rp
from turtle import Turtle, Screen
from PIL import Image

# Turtle setup
to = Turtle()  # Initialize Turtle Class
to.sc = Screen()  # Initialize Screen Class

# Set the screen dimensions (optional)
to.sc.setup(width=800, height=600)

# Set the background image
to.sc.bgpic("x.gif")

# Update the screen
to.sc.update()

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

for _ in range(100):
    to.color(rando_colo())
    to.circle(100)
    to.setheading(to.heading() + 10)
    to.pensize(rp.randint(1, 15))

# Get the canvas
canvas = to.sc.getcanvas()

# Save the canvas as a PostScript file
canvas.postscript(file="image.ps", colormode="color")

# Convert the PostScript file to a WebP file using PIL
img = Image.open("image.ps")

# --- Exiting on click function
to.sc.exitonclick()
