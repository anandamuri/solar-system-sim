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
window.setup(1280, 720)  # dimensions
window.bgcolor("black")  # screen color
window.tracer(0)
window.title("Python Solar System Model")  # window title

# instructions
instructions = turtle.Turtle()
instructions.penup()
instructions.goto(50, 50)
instructions.color("white")
instructions.pendown()
instructions.write("Welcome to the Python Solar System Model!\nClick the respective solar labels to open the "
                   "informative section.", align="left", font=("Arial", 14, "bold"))
instructions.color("black")

scale = 0.75

# making the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.fillcolor("gold")
sun.shapesize(scale * 8)
sun.goto(-400, 0)

# headers
headers = turtle.Turtle()
headers.color("black")
headers.penup()  # CHANGE THIS TO REMOVE LINE
headers.color("black")
headers.goto(sun.xcor(), -75)
headers.write("Not to Scale", align="center", font=("Arial", 7, "bold"))
headers.penup()
headers.goto(0, 300)
headers.color("white")
headers.write("Python Solar System Model", align="center", font=("Arial", 14, "bold"))
headers.penup()
headers.goto(0, -1000)

# drawing information box
info_box = turtle.Turtle()
info_box.goto(0, -200)
info_box.color("white")
info_box.pendown()
for a in range(2):
    info_box.forward(550)
    info_box.left(90)
    info_box.forward(450)
    info_box.left(90)
info_box.color("black")

# testing button abilities
info = turtle.Turtle()
info.color("black")
info.penup()

# info chart for planets
info_chart = turtle.Turtle()
info_chart.color("black")

trait = turtle.Turtle()
trait.color("black")

belt_button = turtle.Turtle()
belt_button.color("black")


class DrawBodies(turtle.Turtle):  # adds turtle to function and sets up class
    def __init__(self, orbit_distance, fill, border, size, revolve):  # initializes attributes of object
        super().__init__()
        self.orbit_distance = scale * orbit_distance
        self.color(border, fill)  # color
        self.up()  # path lines arent drawn
        self.shapesize(scale * size, scale * size)  # size
        self.shape("circle")  # shape is circle
        self.revolve = revolve
        self.angle = random.randint(int(0.01), int(0.05))  # angle is 0 to 0.05

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


def draw_charts():
    info_chart.pendown()
    info_chart.color("black")
    info_chart.goto(350, -200)
    info_chart.color("white")

    for k in range(2):
        info_chart.forward(200)
        info_chart.left(90)
        info_chart.forward(450)
        info_chart.left(90)

    info_chart.forward(100)
    info_chart.left(90)
    info_chart.forward(450)
    info_chart.color("black")
    info_chart.penup()
    info_chart.right(90)

    for y in range(9):
        info_chart.penup()
        info_chart.color("white")
        info_chart.goto(350, y * 50 - 200)
        info_chart.pendown()
        info_chart.forward(200)
        if y == 8:
            info_chart.color("black")
            info_chart.forward(100)


def display_trait(v_list, align, font_type):
    trait.write(v_list, align=align, font=("Arial", 9, font_type))


def write_traits(value):
    trait.goto(400, -225)
    trait.color("white")
    trait.penup()

    info_trait = ["Density", "Mass", "Radius", "Revolution\n   Period", "Rotation\n Period", "Distance\nfrom Sun",
                  "Temperature", "Rings", "Moons"]

    info_trait_belts = ["Density of \nAsteroids", "Mass of \nAsteroids", "Length of\nAsteroids",
                        "Revolution\n   Period", "Width", "Distance\nfrom Sun", "Asteroid Count", "Composition",
                        "Shape of Belt"]

    info_trait_sun = ["Density", "Mass", "Radius", "Magnetic Field \n     Strength", "Rotation\n Period", "Luminosity",
                      "Temperature", "Type of Star", "Moons"]

    info_trait_descriptions = ["Accounts for 99.86% of the mass in the solar system.\n\n"
                               "One million Earth's could fit inside the Sun.\n\n"
                               "The energy created by the Sun’s core is nuclear fusion.\n\n"
                               "The Sun is traveling at 220 km per second.\n\n"
                               "The Sun is halfway through its life.\n\n"
                               "The Sun rotates more quickly at its equator than its poles.\n\n"
                               "The Sun has a powerful magnetic field.\n\n"
                               "Temperatures can reach 15 million degrees celsius.\n\n"
                               "Layers: the photosphere, chromosphere, and corona.\n\n",

                               "Mercury is the closest planet to the Sun.\n\n"
                               "Not only is Mercury the smallest planet, while also shrinking.\n\n"
                               "Mercury has the most craters in the solar system.\n\n"
                               "Mercury was named after the roman god of commerce.\n\n"
                               "Mercury has some extreme temperature changes.\n\n"
                               "The days are very long in Mercury.\n\n"
                               "There is a piece of Mercury here on Earth.\n\n"
                               "Mercury goes through phases just like the Moon.\n\n"
                               "Only two spacecraft have been sent to study Mercury.\n\n",

                               "Venus is hotter than Mercury, even if it's farther from the Sun.\n\n"
                               "Unlike the other planets, Venus spins clockwise on its axis.\n\n"
                               "Venus is the second brightest natural object in the night sky.\n\n"
                               "Venus has 90 times the atmospheric pressure of the Earth.\n\n"
                               "Named after the Roman goddess of love and beauty.\n\n"
                               "The first planet to be plotted as it moves across the sky.\n\n"
                               "Its atmosphere contains sulphuric acid.\n\n"
                               "Venus has a surface of volcanoes, rifts, and mountains.\n\n"
                               "Venus is often called Earth's twin.\n\n",

                               "Earth is almost a sphere.\n\n"
                               "Earth's core is as hot as the Sun's surface.\n\n"
                               "Earth is radioactive and generates 40 terawatts of heat.\n\n"
                               "Earth is mostly iron, oxygen, and silicon.\n\n"
                               "70% of the Earth’s surface is covered in water.\n\n"
                               "The Earth’s molten iron core creates a magnetic field.\n\n"
                               "Earth is the only planet known to have life.\n\n"
                               "Earth's moon is also called Luna.\n\n"
                               "Earth has more than a million known species.\n\n",

                               "Named after the Roman god of war.\n\n"
                               "Mars is also known as the red planet.\n\n"
                               "Mars is the second smallest planet in the solar system.\n\n"
                               "Has the highest mountain in our system: Olympus Mons.\n\n"
                               "You could jump three times higher on Mars than on earth.\n\n"
                               "Mars has two moons - Phobos and Deimos.\n\n"
                               "The first to land on Mars was the Viking landers in 1976.\n\n"
                               "Has the longest valley in the solar system- Valles Marineris.\n\n"
                               "On Mars, the sun appears about half the size as on Earth.\n\n",

                               "Jupiter is the largest planet in the solar system.\n\n"
                               "Jupiter is the fastest spinning planet in the solar system.\n\n"
                               "The clouds on Jupiter are only 50 km thick.\n\n"
                               "Atmospheric clouds are made of ammonia crystals.\n\n"
                               "The great red spot is a planetary-sized storm.\n\n"
                               "Jupiter’s magnetic field is 14 times stronger than Earth’s.\n\n"
                               "Jupiter's moon count is increasing.\n\n"
                               "You can see Jupiter with your own eyes.\n\n"
                               "Jupiter is the third brightest object in the solar system.\n\n",

                               "The most distant planet that can be seen with the naked eye.\n\n"
                               "Known to the Babylonians and Far Eastern observers.\n\n"
                               "Saturn is the flattest planet.\n\n"
                               "Saturn's upper atmosphere is divided into bands of clouds.\n\n"
                               "Saturn is the least dense planet in the solar system.\n\n"
                               "Saturn has only been visited 4 times by spacecraft.\n\n"
                               "Saturn is a gas giant made of hydrogen and helium.\n\n"
                               "Its rings are made of ice, dust, and rock.\n\n"
                               "Saturn's rings are the only ones that can be seen from Earth.\n\n",

                               "Uranus is the coldest planet in the solar system.\n\n"
                               "A season on Uranus lasts one long day – 42 years.\n\n"
                               "Uranus is the second-least dense planet.\n\n"
                               "Uranus has the third-largest diameter in our solar system.\n\n"
                               "Uranus was discovered by William Herschel.\n\n"
                               "Uranus is the only planet with a tilt of 97.77 degrees.\n\n"
                               "Name is a reference to the Greek god of the sky.\n\n"
                               "You can see Uranus with the unaided eye.\n\n"
                               "Atmosphere composed of hydrogen, helium, and methane.\n\n",

                               "Neptune is the last discovered planet in our solar system.\n\n"
                               "Neptune is the smallest gas giant.\n\n"
                               "A year on Neptune lasts 165 Earth years.\n\n"
                               "Neptune is named after the Roman god of the sea.\n\n"
                               "Neptune has 6 faint rings.\n\n"
                               "Neptune has the strongest winds in the solar system.\n\n"
                               "Neptune's surface gravity is almost Earth-like.\n\n"
                               "Neptune is the coldest planet in the solar system.\n\n"
                               "The only planet in our system not visible to the naked eye.\n\n",

                               "Asteroids are irregularly shaped.\n\n"
                               "Giuseppe was the first one to discover an asteroid in 1801.\n\n"
                               "Johann Titius was the first one to discover the asteroid belt.\n\n"
                               "Some are like pebbles and some are more than 400 km.\n\n"
                               "The entire belt is made up of billions of bodies.\n\n"
                               "Average distance between two asteroids is 600,000 miles.\n\n"
                               "The average surface temperature of an asteroid is -73°C.\n\n"
                               "Asteroids are leftovers of the early solar system.\n\n"
                               "Asteroids contain valuable metals – nickel, iron and titanium.\n\n",

                               "The Kuiper Belt is a donut-shaped disc beyond Neptune.\n\n"
                               "Its asteroids are ice-based with methane and ammonia.\n\n"
                               "It extends from 30 AU to approximately 50 AU.\n\n"
                               "It is over 20 times wider than the Asteroid Belt.\n\n"
                               "It contains dwarf planets: Pluto, Haumea, and Makemake.\n\n"
                               "Named after Gerard Kuiper.\n\n"
                               "It was discovered in 1992 by astronomers Jewitt and Luu.\n\n"
                               "Is the remnants from the formation of the solar system.\n\n"
                               "If not for Neptune, it would’ve been a planet.\n\n"]

    info_value = [["1408 kg/m^3", "1.99 × 10^30 kg", "6.96 × 10^5 km", "~1 Gauss", "27 days", "1 L☉",
                   "15 × 10^6°C", "Yellow Dwarf", "4"],
                  ["5427 kg/m^3", "3.29 × 10^23 kg", "2440 km", "87.97 days", "58.6 days", "5.8 × 10^7 km",
                   "-180°C to 430°C", "None", "None"],
                  ["5243 kg/m^3", "4.87 × 10^24 kg", "6051.8 km", "225 days", "243 days", "1.08 × 10^8 km",
                   "475 °C", "None", "None"],
                  ["5514 kg/m^3", "5.97 × 10^24 kg", "6378 km", "365.26 days", "0.99 days", "1.49 × 10^8 km",
                   "-25°C to 45°C", "None", "1"],
                  ["3933 kg/m^3", "6.42 × 10^23 kg", "6779 km", "1.88 years", "1.03 days", "2.28 × 10^8 km",
                   "-153°C to 20°C", "None", "2"],
                  ["1326 kg/m^3", "1.89 × 10^27 kg", "71492 km", "11.86 years", "0.41 days", "7.79 × 10^8 km",
                   "-160°C to -100°C", "Yes", "79"],
                  ["687 kg/m^3", "5.68  × 10^26 kg", "60268 km", "29.46 years", "0.45 days", "1.43 × 10^9 km",
                   "-173°C to -113°C", "Yes", "82"],
                  ["1318 kg/m^3", "8.681 × 10^25 kg", "25362 km", "84.01 years", "0.72 days", "4.5 × 10^8 km",
                   "-195°C to -218°C", "Yes", "27"],
                  ["1638 kg/m^3", "1.024 × 10^26 kg", "24622 km", "164.79 years", "0.67 days", "2.9 × 10^8 km",
                   " -218 °C to -200 °C", "Yes", "14"],
                  ["< 5.32 g/cm^3", "3.2 × 10^21 kg", "1 to ~100 km", "4.5 years", "149.7 × 10^6 km",
                   "329.1 to 478.7\n   × 10^6 km", "~1.9 × 10^6", "Rocky", "Torus Shape"],
                  ["> 1.5 g/cm^3", "1.36 × 10^23 kg", "30 to 55 km", "10500 years", "1.05 x 10^10 km",
                   "    4.4 × 10^9 to \n1.49 × 10^10 km", "1 x 10^8", "Icy", "Donut Shape"]]

    for k in range(2):
        for u in range(9):
            if k == 0:
                if value == 0:
                    if 3 <= u <= 4:
                        trait.goto(400, -190 + u * 50)
                        display_trait(info_trait_sun[u], "center", "bold")
                    else:
                        trait.goto(400, -185 + u * 50)
                        display_trait(info_trait_sun[u], "center", "bold")
                elif 9 <= value <= 10:
                    if 0 <= u <= 3 or u == 5:
                        trait.goto(400, -190 + u * 50)
                        display_trait(info_trait_belts[u], "center", "bold")
                    else:
                        trait.goto(400, -185 + u * 50)
                        display_trait(info_trait_belts[u], "center", "bold")
                else:
                    if 3 <= u <= 5:
                        trait.goto(400, -190 + u * 50)
                        display_trait(info_trait[u], "center", "bold")
                    else:
                        trait.goto(400, -185 + u * 50)
                        display_trait(info_trait[u], "center", "bold")
            if k == 1:
                if value == 9:
                    if u == 5:
                        trait.goto(500, -190 + u * 50)
                        display_trait(info_value[value][u], "center", "bold")
                    else:
                        trait.goto(500, -185 + u * 50)
                        display_trait(info_value[value][u], "center", "bold")
                elif value == 10:
                    if u == 5:
                        trait.goto(500, -190 + u * 50)
                        display_trait(info_value[value][u], "center", "bold")
                    else:
                        trait.goto(500, -185 + u * 50)
                        display_trait(info_value[value][u], "center", "bold")
                else:
                    trait.goto(500, -185 + u * 50)
                    display_trait(info_value[value][u], "center", "bold")

            trait.color("white")
            trait.goto(15, -150)
            display_trait(info_trait_descriptions[value], "left", "normal")
            trait.penup()
            trait.goto(1000, 0)


def draw_belts_button():
    belt_button.penup()
    belt_button.color("white")
    belt_button.goto(15, 158)
    belt_button.dot(10, "grey")
    belt_button.goto(35, 150)
    belt_button.write("Asteroid Belt", align="left", font=("Arial", 9, "bold"))

    belt_button.goto(125, 158)
    belt_button.dot(10, "grey")
    belt_button.goto(145, 150)
    belt_button.write("Kuiper Belt", align="left", font=("Arial", 9, "bold"))
    belt_button.penup()
    belt_button.goto(0, 1000)


def concise_clear():
    info.clear()
    trait.clear()
    info_chart.clear()
    belt_button.clear()
    instructions.clear()  # hiding headers option
    info.penup()
    info.goto(10, 200)
    info.color("white")
    draw_charts()


def info_buttons(x, y):
    if -495 < x < -395 and -300 < y < -225:
        concise_clear()
        write_traits(0)
        info.write("Sun", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif -395 < x < -295 and -300 < y < -225:
        concise_clear()
        info.write("Mercury", align="left", font=("Arial", 14, "bold"))
        write_traits(1)
        info.goto(45, 175)
        info.color("black")
        info.goto(45, -175)
    elif -295 < x < -195 and -300 < y < -225:
        concise_clear()
        write_traits(2)
        info.write("Venus", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif -195 < x < -95 and -300 < y < -225:
        concise_clear()
        write_traits(3)
        info.write("Earth", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif -95 < x < 5 and -300 < y < -225:
        concise_clear()
        write_traits(4)
        info.write("Mars", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif 5 < x < 105 and -300 < y < -225:
        concise_clear()
        write_traits(5)
        info.write("Jupiter", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif 105 < x < 205 and -300 < y < -225:
        concise_clear()
        write_traits(6)
        info.write("Saturn", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif 205 < x < 305 and -300 < y < -225:
        concise_clear()
        write_traits(7)
        info.write("Uranus", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif 305 < x < 405 and -300 < y < -225:
        concise_clear()
        write_traits(8)
        info.write("Neptune", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif 405 < x < 505 and -300 < y < -225:
        info.clear()
        trait.clear()
        info_chart.clear()
        instructions.clear()
        info.goto(10, 200)
        info.color("white")
        draw_charts()
        write_traits(9)
        draw_belts_button()
        info.write("Asteroid Belt", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif 10 < x < 110 and 125 < y < 175:
        info.clear()
        trait.clear()
        info.goto(10, 200)
        info.color("white")
        write_traits(9)
        draw_belts_button()
        info.write("Asteroid Belt", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)
    elif 110 < x < 210 and 125 < y < 175:
        info.clear()
        trait.clear()
        info.goto(10, 200)
        info.color("white")
        write_traits(10)
        draw_belts_button()
        info.write("Kuiper Belt", align="left", font=("Arial", 14, "bold"))
        info.color("black")
        info.goto(45, -175)


turtle.onscreenclick(info_buttons, 1, add=False)

# planetary rings
jupiter_rings = DrawBodies(200, "black", "brown4", 3.3, sun)
saturn_rings = DrawBodies(270, "black", "tan", 3.2, sun)
saturn_rings2 = DrawBodies(270, "black", "tan", 3, sun)
uranus_rings = DrawBodies(320, "black", "light blue", 2, sun)
neptune_rings = DrawBodies(360, "black", "blue", 2.15, sun)
neptune_rings2 = DrawBodies(360, "black", "blue", 1.95, sun)

# planets (sizes are based on the sun)
mercury = DrawBodies(85, "light grey", "light grey", 0.2, sun)
venus = DrawBodies(100, "light green", "light green", 0.6, sun)
earth = DrawBodies(125, "aqua", "aqua", 0.6, sun)
mars = DrawBodies(140, "firebrick2", "firebrick2", 0.2, sun)
jupiter = DrawBodies(200, "brown", "brown", 2.05, sun)
saturn = DrawBodies(270, "tan", "tan", 1.75, sun)
uranus = DrawBodies(320, "light blue", "light blue", 0.75, sun)
neptune = DrawBodies(360, "blue", "blue", 0.70, sun)

# info tabs (optional)
# mercury_info_tabs = DrawLabelTabs(-300, -250, "light grey")
# venus_info_tabs = DrawLabelTabs(-200, -250, "light green")
# earth_info_tabs = DrawLabelTabs(-100, -250, "aqua")
# mars_info_tabs = DrawLabelTabs(0, -250, "firebrick2")
# jupiter_info_tabs = DrawLabelTabs(100, -250, "brown")
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

# moons
earth_list = []
earth_angle = 0.001

for i in range(1):  # number of moons
    earth_moon = DrawBodies(14, "grey", "grey", 0.07, earth)  # 0.0499001939
    earth_moon.penup()
    earth_list.append(earth_moon)
    earth_moon.angle += earth_angle
    earth_angle += 9

mars_list = []
mars_angle = 0.001

for i in range(2):  # number of moons
    mars_moon = DrawBodies(5, "grey", "grey", 0.07, mars)
    mars_moon.penup()
    mars_list.append(mars_moon)
    mars_moon.angle += mars_angle
    mars_angle += 9

jupiter_list = []
jupiter_angle = 0.001

for i in range(79):  # number of moons
    jupiter_moon = DrawBodies(random.randint(25, 30), "grey", "grey", 0.07, jupiter)
    jupiter_moon.penup()
    jupiter_list.append(jupiter_moon)
    jupiter_moon.angle += jupiter_angle
    jupiter_angle += 0.5

saturn_list = []
saturn_angle = 0.001

for i in range(82):  # number of moons
    saturn_moon = DrawBodies(random.randint(20, 25), "grey", "grey", 0.07, saturn)
    saturn_moon.penup()
    saturn_list.append(saturn_moon)
    saturn_moon.angle += saturn_angle
    saturn_angle += 1

uranus_list = []
uranus_angle = 0.001

for i in range(27):  # number of moons
    uranus_moon = DrawBodies(random.randint(15, 20), "grey", "grey", 0.07, uranus)
    uranus_moon.penup()
    uranus_list.append(uranus_moon)
    uranus_moon.angle += uranus_angle
    uranus_angle += 15

neptune_list = []
neptune_angle = 0.001

for i in range(14):  # number of moons
    neptune_moon = DrawBodies(random.randint(10, 15), "grey", "grey", 0.07, neptune)
    neptune_moon.penup()
    neptune_list.append(neptune_moon)
    neptune_moon.angle += neptune_angle
    neptune_angle += 20

asteroid_list = []
asteroid_angle = 0.001

for i in range(300):
    asteroid = DrawBodies(random.randint(150, 160), "grey", "grey", 0.1, sun)
    asteroid.penup()
    asteroid_list.append(asteroid)
    asteroid.angle += asteroid_angle
    asteroid_angle += 0.09

kuiper_list = []
kuiper_angle = 0.001

for i in range(300):
    kuiper = DrawBodies(random.randint(365, 495), "grey", "grey", 0.15, sun)
    kuiper.penup()
    kuiper_list.append(kuiper)
    kuiper.angle += kuiper_angle
    kuiper_angle += 0.09

trojan_list = []
trojan_angle = 0

for a in range(4):
    trojan_angle = 90

    for i in range(9):
        trojan = DrawBodies(random.randint(190, 200), "grey", "grey", 0.15, sun)
        trojan.penup()
        trojan_list.append(trojan)
        trojan.angle += trojan_angle

        if a == 0:
            trojan_angle += 3
        elif a == 1:
            trojan_angle += 3.1
        elif a == 2:
            trojan_angle += 3.2
        elif a == 3:
            trojan_angle += 3.1
        elif a == 4:
            trojan_angle += 3

Solar_Bodies = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
Solar_Rings = [jupiter_rings, saturn_rings, saturn_rings2, uranus_rings, neptune_rings,
               neptune_rings2]

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
            a.solar_orbit(59.5)
        elif a == Solar_Bodies[5]:
            a.solar_orbit(-90)
        elif a == Solar_Bodies[6]:
            a.solar_orbit(270)
        elif a == Solar_Bodies[7]:
            a.solar_orbit(-150)

    for a in Solar_Rings:
        if a == Solar_Rings[0]:
            a.solar_orbit(59.5)
        elif a == Solar_Rings[1]:
            a.solar_orbit(-90)
        elif a == Solar_Rings[2]:
            a.solar_orbit(-90)
        elif a == Solar_Rings[3]:
            a.solar_orbit(270)
        elif a == Solar_Rings[4]:
            a.solar_orbit(-150)
        elif a == Solar_Rings[5]:
            a.solar_orbit(-150)

    for b in earth_list:
        b.solar_orbit(0)
        b.angle += 0.14  # 1.352814815 * 10^-1

    for c in mars_list:
        c.solar_orbit(0)
        c.angle += 0.05

    for d in jupiter_list:
        d.solar_orbit(0)
        d.angle += 0.03

    for e in saturn_list:
        e.solar_orbit(0)
        e.angle += 0.03

    for f in uranus_list:
        f.solar_orbit(0)
        f.angle += 0.07

    for g in neptune_list:
        g.solar_orbit(0)
        g.angle += 0.07

    for h in asteroid_list:
        h.solar_orbit(0)
        h.angle += 0.009

    for i in kuiper_list:
        i.solar_orbit(0)
        i.angle += 0.002

    for j in trojan_list:
        j.solar_orbit(0)
        j.angle += 0.005

    # if earth.angle > 10:  # hiding headers option
    #     headers.clear()

    # planetary ring angles
    jupiter_rings.angle += 0.005  # 8.4317032 * 10^-4
    saturn_rings.angle += 0.0034  # 3.39443313 * 10^-4
    saturn_rings2.angle += 0.0034  # 3.39443313 * 10^-4
    uranus_rings.angle += 0.0012  # 1.190334484 * 10^-4
    neptune_rings.angle += 0.0006  # 6.068329389 * 10^-5
    neptune_rings2.angle += 0.0006  # 6.068329389 * 10^-5

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
