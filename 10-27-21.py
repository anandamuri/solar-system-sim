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
        self.color(fill)  # color
        self.up()  # path lines arent drawn
        self.shapesize(size, size)  # size
        self.shape("circle")  # shape is circle
        self.revolve = revolve
        self.angle = random.randint(int(0.01), int(0.05))   # angle is 0 to 0.05

    def solar_orbit(self):
        xcor = self.orbit_distance * cos(self.angle)  # cos corresponds to x
        ycor = self.orbit_distance * sin(self.angle)  # sin corresponds to y
        # coordinate of the orbited object + curved coordinate trajectory
        self.goto(self.revolve.xcor() + xcor, self.revolve.ycor() + ycor)


# calling the function
mercury = DrawPlanets(210, "grey", 0.5, sun)
venus = DrawPlanets(250, "yellow", 1, sun)
earth = DrawPlanets(300, "aqua", 2, sun)
mars = DrawPlanets(350, "red", 2, sun)
jupiter = DrawPlanets(500, "brown", 5, sun)
saturn = DrawPlanets(650, "tan", 3, sun)
uranus = DrawPlanets(700, "light blue", 3, sun)
neptune = DrawPlanets(850, "blue", 3, sun)

Solar_Bodies = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

while True:
    window.update()  # updates the window
    for a in Solar_Bodies:
        a.solar_orbit()

    mercury.angle += 0.04
    venus.angle += 0.03
    earth.angle += 0.02
    mars.angle += 0.01
    jupiter.angle += 0.004
    saturn.angle += 0.003
    uranus.angle += 0.002
    neptune.angle += 0.001

    time.sleep(0.01)
