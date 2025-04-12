# imports
import turtle

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

# making the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.fillcolor("yellow")
sun.shapesize(20)
# sun.begin_fill()  # redundant
# sun.end_fill()  # redundant


while True:
    window.update()  # updates the window
