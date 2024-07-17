# Day 18 - Turtle and GUI

# Importing the turtle module

from turtle import Turtle, Screen

ina_tut = Turtle()

# Shapes and colors
ina_tut.shape("turtle")
ina_tut.color("coral")
ina_tut.shapesize(stretch_wid=3, stretch_len=3, outline=1)
ina_tut.screen.bgcolor("#020617")


















# Show Screen - Exit Screen with click
ina_tut_screen = Screen()
ina_tut_screen.exitonclick()