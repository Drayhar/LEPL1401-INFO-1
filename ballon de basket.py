import turtle
from math import cos, sin
def ballon(rayon, couleur = "black"):
    def deplacement(x, y): # lève la tortue et la déplace en x, y
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    #définition tortue
    turtle.shape("turtle")
    turtle.color(couleur)
    turtle.width(rayon / 50)
    turtle.fillcolor("orange")

    #cercle autour
    turtle.begin_fill()
    deplacement(rayon, 0)
    turtle.left(90)
    turtle.circle(rayon, 360)
    turtle.end_fill()

    #les deux lignes centrales
    deplacement(0, -rayon)
    turtle.forward(2 * rayon)
    deplacement(rayon, 0)
    turtle.left(90)
    turtle.forward(2 * rayon)

    #ligne arrondie
    deplacement(rayon * sin(45), rayon * cos(-45))
    turtle.circle(rayon / 2, 180)
    deplacement(rayon * sin(-45), rayon * cos(45))
    turtle.circle(rayon / -2, 180)

    turtle.hideturtle()
    turtle.done()

ballon(int(input("Quelle taille de ballon ?\n")))


import turtle
from math import pi, sin, cos
import random
import time
turtle.speed(10)
def pave(x, y, arete, color1, color2, color3):
    def deplacement(x, y):
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    def hexagone(color):
        turtle.fillcolor(color)
        angle = 120
        turtle.begin_fill()
        for j in range(4):  # un parallélépipède
            turtle.forward(arete)
            turtle.left(angle)
            angle = 180 - angle
        turtle.end_fill()
        turtle.right(120)
    deplacement(x, y)
    hexagone(color1)
    deplacement(x, y)
    hexagone(color2)
    deplacement(x, y)
    hexagone(color3)

turtle.hideturtle()
time.sleep(3)

while True:
    pave(random.randint(-300,300), random.randint(-300, 300), random.randint(10, 50), "black", "red", "blue")
    pave(random.randint(-300, 300), random.randint(-300, 300), random.randint(10, 50), "white", "grey", "black")

