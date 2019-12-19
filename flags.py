#Programme dessinant plusieurs drapeaux à l'aide du module Turtle
#Vincent Bauffe, octobre 2019

import turtle                # module des graphiques tortue
tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed("fastest")      # tracé rapide

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def rectangle(width, height, color):
    """Trace un rectangle plein de taille `width * height` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du rectangle.
    post: Le rectangle a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def three_color_flag(width, color1, color2, color3):
    """
    Trace un drapeau à trois bandes de largeur width et de hauteur 2 / 3 de width
    :param width: La tortue est initialisée et au début de la forme
    :return: Le drapeau est tracé sur la droite de la tortue et elle revient au départ
    """
    rectangle(int((1/3) * width), int((2/3) * width), color1)
    tortue.forward(int((1/3) * width))
    rectangle(int((1 / 3) * width), int((2 / 3) * width), color2)
    tortue.forward(int((1 / 3) * width))
    rectangle(int((1 / 3) * width), int((2 / 3) * width), color3)
    tortue.backward(int((2 / 3) * width))

def belgian_flag(width):
    """
    Trace un drapeau belge de largeur width et de hauteur 2 / 3 de width
    :param width: La tortue est initialisée et au début de la forme
    :return: Le drapeau est tracé sur la droite de la tortue et elle revient au départ
    """
    three_color_flag(width, "black", "yellow", "red")

def french_flag(width):
    """
    Trace un drapeau français
    :param width: largeur
    :return: drapeau français
    """
    three_color_flag(width, "blue", "white", "red")

def horizontal_flag(width, color1, color2, color3):
    """
    Réalisation d'un drapeau horizontal
    :param width: largeur
    :param color1:
    :param color2:
    :param color3:
    :return: drapeau horizontal
    """
    rectangle(width, int((2 / 9) * width), color1)
    tortue.right(90)
    tortue.forward(int((2 / 9) * width))
    tortue.right(-90)
    rectangle(width, int((2 / 9) * width), color2)
    tortue.right(90)
    tortue.forward(int((2 / 9) * width))
    tortue.right(-90)
    rectangle(width, int((2 / 9) * width), color3)
    tortue.left(90)
    tortue.forward(int((4 / 9) * width))
    tortue.right(90)

def dutch_flag(width):
    """
    drapeau hollandais
    :param width: largeur
    :return: drapeau hollandais
    """
    horizontal_flag(width, "red", "white", "blue")

def german_flag(width):
    """
    drapeau allemand
    :param width: largeur
    :return: drapeau allemand
    """
    horizontal_flag(width, "black", "red", "yellow")

def luxembourg_flag(width):
    """
    drapeau luxembourgeois
    :param width: largeur
    :return: drapeau luxembourgeois
    """
    horizontal_flag(width, "red", "white", "cyan")

def yellow_star(width):
    """
    étoile jaune
    :param width: largeur
    :return: étoile jaune
    """
    tortue.color("yellow")
    tortue.pendown()
    tortue.begin_fill()
    for i in range(5):
        tortue.forward(int(width / 3 ))
        tortue.right(144)
    tortue.end_fill()
    tortue.penup()

def european_flag(width):
    """
    drapeau européen
    :param width: largeur
    :return: drapeau européen
    """
    rectangle(width, int((2 / 3) * width), "blue")
    tortue.forward(float(width / 2.15))
    tortue.right(90)
    tortue.forward(int(width) / 3)
    tortue.left(90)
    for angle in range(0, 360, 360 // 12):
        tortue.left(angle)
        tortue.forward(int(width / 5))
        tortue.right(angle)
        yellow_star(int(width / 5))
        tortue.left(angle)
        tortue.backward(int(width / 5))
        tortue.right(angle)

tortue.penup()
tortue.goto(-300, 300)

for i in range(3): #Les 3 drapeaux belges
    belgian_flag(100)
    tortue.forward(100 * 2)
tortue.goto(-200, 200)
european_flag(300)
tortue.goto(-300, -50)
dutch_flag(100)
tortue.forward(100 * 1.4)
german_flag(100)
tortue.forward(100 * 1.4)
luxembourg_flag(100)
tortue.forward(100 * 1.4)
french_flag(100)

tortue.hideturtle()
turtle.exitonclick()