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
instructions.write("Welcome to the Python Solar System Model!\nClick the respective solar labels to open the "
                   "informative section.", align="center", font=("Arial", 14, "bold"))
instructions.color("black")

# headers
headers = turtle.Turtle()
headers.penup()
headers.color("black")
headers.color("white")
headers.goto(-400, -75)
headers.write("Not to Scale", align="center", font=("Arial", 7, "bold"))
headers.color("black")
headers.goto(0, 300)
headers.color("white")
headers.write("Python Solar System Model", align="center", font=("Arial", 14, "bold"))
headers.color("black")
headers.goto(0, -1000)

scale = 0.75

# making the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.fillcolor("gold")
sun.shapesize(scale * 8)
sun.goto(-400, 0)


class DrawBodies(turtle.Turtle):  # adds turtle to function and sets up class
    def __init__(self, orbit_distance, fill, border, size, revolve):  # initializes attributes of object
        super().__init__()
        self.orbit_distance = scale * orbit_distance
        self.color(border, fill)  # color
        self.up()  # path lines arent drawn
        self.shapesize(scale * size, scale * size)  # size
        self.shape("circle")  # shape is circle
        self.revolve = revolve
        self.angle = random.randint(int(0.01), int(0.05))   # angle is 0 to 0.05

    def solar_orbit(self, position):
        xcor = self.orbit_distance * cos(self.angle - position)  # cos corresponds to x
        ycor = self.orbit_distance * sin(self.angle - position)  # sin corresponds to y
        # coordinate of the orbited object + curved coordinate trajectory
        self.goto(self.revolve.xcor() + xcor, self.revolve.ycor() + ycor)


# optional
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
        self.goto(x_location - 30, y_location - 50)
        self.penup()
        self.dot(10, color)
        self.goto(x_location + 20, y_location - 58)
        self.color("white")
        self.write(text, align="center", font=("Arial", 9, "bold"))
        self.color("black")
        self.backward(50)


# testing button abilities
info = turtle.Turtle()
info.color("black")
info.penup()


def info_buttons(x, y):
    if -495 < x < -395 and -300 < y < -225:
        info.clear()
        instructions.clear()  # hiding headers option
        info.penup()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE0", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif -395 < x < -295 and -300 < y < -225:
        info.clear()
        instructions.clear()  # hiding headers option
        info.penup()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE1", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif -295 < x < -195 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.penup()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE2", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif -195 < x < -95 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE3", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif -95 < x < 5 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE4", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 5 < x < 105 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE5", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 105 < x < 205 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE6", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 205 < x < 305 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE7", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 305 < x < 405 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE8", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)
    elif 405 < x < 505 and -300 < y < -225:
        info.clear()
        instructions.clear()
        info.goto(0, 200)
        info.color("white")
        info.write("HERE9", align="center", font=("Arial", 9, "bold"))
        info.color("black")
        info.goto(0, 225)


turtle.onscreenclick(info_buttons, 1, add=False)

# planets (sizes are based on the sun) (All bodies are currently 1037.5 times larger than scale)
mercury = DrawBodies(85, "light grey", "light grey", 0.2, sun)
venus = DrawBodies(100, "light green", "light green", 0.6, sun)
earth = DrawBodies(125, "aqua", "aqua", 0.6, sun)
mars = DrawBodies(140, "firebrick2", "firebrick2", 0.2, sun)
jupiter = DrawBodies(200, "brown", "brown", 2.05, sun)
saturn = DrawBodies(250, "tan", "tan", 1.75, sun)
uranus = DrawBodies(290, "light blue", "light blue", 0.75, sun)
neptune = DrawBodies(330, "blue",  "blue", 0.70, sun)

# info tabs (optional)
# mercury_info_tabs = DrawLabelTabs(-300, -250, "light grey")
# venus_info_tabs = DrawLabelTabs(-200, -250, "light green")
# earth_info_tabs = DrawLabelTabs(-100, -250, "aqua")
# mars_info_tabs = DrawLabelTabs(0, -250, "firebrick2")
# jupiter_info_tabs = DrawLabelTabs(100, -250, "brown") v
# saturn_info_tabs = DrawLabelTabs(200, -250, "tan")
# uranus_info_tabs = DrawLabelTabs(300, -250, "light blue")
# neptune_info_tabs = DrawLabelTabs(400, -250, "blue")

# info labels
sun_info = DrawLabel(-450, -200, "gold", "Sun")
mercury_info = DrawLabel(-350, -200, "light grey", "Mercury")
venus_info = DrawLabel(-250, -200, "light green", "Venus")
earth_info = DrawLabel(-150, -200, "aqua", "Earth")
mars_info = DrawLabel(-50, -200, "firebrick2", "Mars")
jupiter_info = DrawLabel(50, -200, "brown", "Jupiter")
saturn_info = DrawLabel(150, -200, "tan", "Saturn")
uranus_info = DrawLabel(250, -200, "light blue", "Uranus")
neptune_info = DrawLabel(350, -200, "blue", "Neptune")
asteroid_info = DrawLabel(450, -200, "grey", "Belts")

Solar_Bodies = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

while True:
    window.update()  # updates the window

    for a in Solar_Bodies:
        if a == Solar_Bodies[0]:
            a.solar_orbit(120)
        elif a == Solar_Bodies[1]:
            a.solar_orbit(270)
        elif a == Solar_Bodies[2]:
            a.solar_orbit(-210)
        elif a == Solar_Bodies[3]:
            a.solar_orbit(0)
        elif a == Solar_Bodies[4]:
            a.solar_orbit(60)
        elif a == Solar_Bodies[5]:
            a.solar_orbit(-90)
        elif a == Solar_Bodies[6]:
            a.solar_orbit(270)
        elif a == Solar_Bodies[7]:
            a.solar_orbit(-150)

    # if earth.angle > 10:  # hiding headers option
    #     headers.clear()

    # planet angles
    mercury.angle += 0.042  # 4.15209731 * 10^-2
    venus.angle += 0.016  # 1.62554517 * 10^-2
    earth.angle += 0.01  # ratios are based on this
    mars.angle += 0.009  # 5.3191489 * 10^-3
    jupiter.angle += 0.005  # 8.4317032 * 10^-4
    saturn.angle += 0.0034  # 3.39443313 * 10^-4
    uranus.angle += 0.0012  # 1.190334484 * 10^-4
    neptune.angle += 0.0006  # 6.068329389 * 10^-5

    time.sleep(0.01)
