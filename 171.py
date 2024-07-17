# Work from 171

from turtle import Turtle, Screen


to = Turtle()  #Intitialize Turtle Class
to.sc = Screen()  # Initialize Screen Class
to.sc.register_shape("ax.gif")  # Initialize Shape
to.color("coral")  # Setting color
to.shapesize(stretch_wid=3, stretch_len=3, outline=1) # Setting size params
to.sc.bgcolor("#020617") # Set Bg Color
to.sc.exitonclick()  # Exiting on click
