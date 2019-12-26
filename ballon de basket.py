import time
import random
from math import pi, sin, cos
from math import cos, sin
import turtle
gaspard = turtle.Turtle()


def ballon(rayon, couleur="black"):
    def deplacement(x, y):  # lève la tortue et la déplace en x, y
        gaspard.up()
        gaspard.goto(x, y)
        gaspard.down()

    # définition tortue
    gaspard.shape("gaspard")
    gaspard.color(couleur)
    gaspard.width(rayon / 50)
    gaspard.fillcolor("orange")

    # cercle autour
    gaspard.begin_fill()
    deplacement(rayon, 0)
    gaspard.left(90)
    gaspard.circle(rayon, 360)
    gaspard.end_fill()

    # les deux lignes centrales
    deplacement(0, -rayon)
    gaspard.forward(2 * rayon)
    deplacement(rayon, 0)
    gaspard.left(90)
    gaspard.forward(2 * rayon)

    # ligne arrondie
    deplacement(rayon * sin(45), rayon * cos(-45))
    gaspard.circle(rayon / 2, 180)
    deplacement(rayon * sin(-45), rayon * cos(45))
    gaspard.circle(rayon / -2, 180)

    gaspard.hideturtle()
    turtle.done()


ballon(int(input("Quelle taille de ballon ?\n")))


gaspard.speed(10)


def pave(x, y, arete, color1, color2, color3):
    def deplacement(x, y):
        gaspard.up()
        gaspard.goto(x, y)
        gaspard.down()

    def hexagone(color):
        gaspard.fillcolor(color)
        angle = 120
        gaspard.begin_fill()
        for _ in range(4):  # un parallélépipède
            gaspard.forward(arete)
            gaspard.left(angle)
            angle = 180 - angle
        gaspard.end_fill()
        gaspard.right(120)
    deplacement(x, y)
    hexagone(color1)
    deplacement(x, y)
    hexagone(color2)
    deplacement(x, y)
    hexagone(color3)


gaspard.hideturtle()
time.sleep(3)

while True:
    pave(random.randint(-300, 300), random.randint(-300, 300),
         random.randint(10, 50), "black", "red", "blue")
    pave(random.randint(-300, 300), random.randint(-300, 300),
         random.randint(10, 50), "white", "grey", "black")
