# Dashed Py

# --- Turtle setup code
from turtle import Turtle, Screen

ina_tut = Turtle()
screen = Screen()
screen.register_shape("ax.gif")
# Setting the shape here
ina_tut.shape("ax.gif")
ina_tut.color("coral")
ina_tut.shapesize(stretch_wid=3, stretch_len=3, outline=1)
screen.bgcolor("#020617")

# ---

# Draw a dashed line

for _ in range(15):
    ina_tut.forward(10)
    ina_tut.penup()
    ina_tut.forward(10)
    ina_tut.pendown()

screen.exitonclick()