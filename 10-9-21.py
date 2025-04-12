# imports
import turtle
import time
import random
from math import *

# setting up the window
window = turtle.Screen()
window.setup(1200, 650)  # dimensions
window.bgcolor("black")  # screen color
window.tracer(0)
window.title("Python Solar System Model")  # window title


# this could be made into a function in future
turtle.color("black")
turtle.goto(0, 275)
turtle.color("white")
turtle.write("Anish Nandamuri", align="center", font=("Arial", 14, "bold"))
turtle.color("black")
turtle.goto(0, 300)
turtle.color("white")
turtle.write("Python Solar System Model", align="center", font=("Arial", 14, "bold"))
turtle.color("black")

# pause screen test
# time.sleep(5)

# making the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.fillcolor("yellow")
sun.shapesize(20)


class DrawPlanets(turtle.Turtle):  # adds turtle to function
    def __init__(self, orbit_distance, fill, size, revolve):  # initializes attributes of object
        super().__init__()
        self.orbit_distance = orbit_distance
        self.color(fill)
        self.up()
        self.shapesize(size, size)
        self.shape("circle")
        self.revolve = revolve
        self.angle = random.randint(int(0.01), int(0.05))

    def solar_orbit(self):
        xcor = self.orbit_distance * cos(self.angle)  # cos corresponds to x
        ycor = self.orbit_distance * sin(self.angle)  # sin corresponds to y
        # coordinate of the orbited object + curved coordinate trajectory
        self.goto(self.revolve.xcor() + xcor, self.revolve.ycor() + ycor)


earth = DrawPlanets(300, "aqua", 2, sun)  # calls the function

Solar_Bodies = [earth]

while True:
    window.update()  # updates the window
    for a in Solar_Bodies:
        a.solar_orbit()

    earth.angle += 0.02

    time.sleep(0.01)  # smoothness
