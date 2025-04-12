# ======================================================================================================================
__author__ = "Anish Nandamuri"
__version__ = "1.0.1"
__school__ = "International Academy East"
__course__ = "MYP Personal Project"
__topic__ = "Python Solar System Model"
__email__ = "nandamuri.anish72@bloomfield.org"
# ======================================================================================================================

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

# instructions
instructions = turtle.Turtle()
instructions.color("black")
instructions.goto(50, 0)
instructions.color("white")
instructions.write("Welcome to the Python Solar System Model!\nClick the respective colored bars to open the "
                   "informative section.", align="center", font=("Arial", 14, "bold"))
instructions.color("black")

# making the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.fillcolor("yellow")
sun.shapesize(20)
sun.goto(-500, 0)


class DrawPlanets(turtle.Turtle):  # adds turtle to function and sets up class
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


class DrawLabelTabs(turtle.Turtle):
    def __init__(self, x_location, y_location, color):
        super().__init__()
        self.goto(x_location - 15, y_location - 35)
        self.shape("square")
        self.shapesize(1, 5)
        self.fillcolor(color)
        self.penup()


class DrawLabel(turtle.Turtle):
    def __init__(self, x_location, y_location, color, text):
        super().__init__()
        self.penup()
        self.goto(x_location, y_location - 50)
        self.penup()
        self.dot(10, color)
        self.goto(x_location + 50, y_location - 58)
        self.color("white")
        self.write(text, align="center", font=("Arial", 9, "bold"))
        self.color("black")
        self.backward(50)


# testing button abilities
info = turtle.Turtle()
info.color("black")
info.penup()


def buttons(x, y):
    if -365 < x < -265 and -300 < y < -225:
        info.clear()
        instructions.clear()  # hiding headers option
        info.penup()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE1", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif -265 < x < -165 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.penup()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE2", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif -165 < x < -65 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE3", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif -65 < x < 35 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE4", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 35 < x < 135 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE5", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 135 < x < 235 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE6", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 235 < x < 335 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE7", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 335 < x < 435 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE8", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)


turtle.onscreenclick(buttons, 1, add=False)

# planets
mercury = DrawPlanets(210, "light grey", 0.5, sun)
venus = DrawPlanets(250, "light green", 1, sun)
earth = DrawPlanets(300, "aqua", 2, sun)
mars = DrawPlanets(350, "firebrick2", 2, sun)
jupiter = DrawPlanets(500, "brown", 5, sun)
saturn = DrawPlanets(650, "tan", 3, sun)
uranus = DrawPlanets(700, "light blue", 3, sun)
neptune = DrawPlanets(850, "blue", 3, sun)

# moons
earth_moon = DrawPlanets(30, "grey", 0.4, earth)

# info tabs
# mercury_info_tabs = DrawLabelTabs(-300, -250, "light grey")
# venus_info_tabs = DrawLabelTabs(-200, -250, "light green")
# earth_info_tabs = DrawLabelTabs(-100, -250, "aqua")
# mars_info_tabs = DrawLabelTabs(0, -250, "firebrick2")
# jupiter_info_tabs = DrawLabelTabs(100, -250, "brown")
# saturn_info_tabs = DrawLabelTabs(200, -250, "tan")
# uranus_info_tabs = DrawLabelTabs(300, -250, "light blue")
# neptune_info_tabs = DrawLabelTabs(400, -250, "blue")

# info labels
mercury_info = DrawLabel(-350, -200, "light grey", "Mercury")
venus_info = DrawLabel(-250, -200, "light green", "Venus")
earth_info = DrawLabel(-150, -200, "aqua", "Earth")
mars_info = DrawLabel(-50, -200, "firebrick2", "Mars")
jupiter_info = DrawLabel(50, -200, "brown", "Jupiter")
saturn_info = DrawLabel(150, -200, "tan", "Saturn")
uranus_info = DrawLabel(250, -200, "light blue", "Uranus")
neptune_info = DrawLabel(350, -200, "blue", "Neptune")

Solar_Bodies = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, earth_moon]


while True:
    window.update()  # updates the window

    for a in Solar_Bodies:
        a.solar_orbit()

    # if earth.angle > 10:  # hiding headers option
    #     headers.clear()

    mercury.angle += 0.04
    venus.angle += 0.03
    earth.angle += 0.02
    mars.angle += 0.01
    jupiter.angle += 0.004
    saturn.angle += 0.003
    uranus.angle += 0.002
    neptune.angle += 0.001

    earth_moon.angle += 0.09

    time.sleep(0.01)
