import turtle                # module des graphiques tortue
tortue = turtle.Turtle()     # crÃ©er une nouvelle tortue
tortue.speed("fastest")      # tracÃ© rapide


def square(size, color):
    """Trace un carrÃ© plein de taille `size` et de couleur `color`.

    pre: `color` spÃ©cifie une couleur.
         La tortue `tortue` est initialisÃ©e.
         La tortue est placÃ©e Ã  un sommet et orientÃ©e en direction d'un
         cÃ´tÃ© du carrÃ©.
    post: Le carrÃ© a Ã©tÃ© tracÃ© sur la droite du premier cÃ´tÃ©.
          La tortue est Ã  la mÃªme position et orientation qu'au dÃ©part.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for _ in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()


def rectangle(width, height, color):
    """Trace un rectangle plein de taille `width * height` et de couleur `color`.

    pre: `color` spÃ©cifie une couleur.
         La tortue `tortue` est initialisÃ©e.
         La tortue est placÃ©e Ã  un sommet et orientÃ©e en direction d'un
         cÃ´tÃ© du rectangle.
    post: Le rectangle a Ã©tÃ© tracÃ© sur la droite du premier cÃ´tÃ©.
          La tortue est Ã  la mÃªme position et orientation qu'au dÃ©part.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for _ in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()


def three_color_flag(width, color1, color2, color3):
    """
    Trace un drapeau Ã  trois bandes de largeur width et de hauteur 2 / 3 de width
    :param width: La tortue est initialisÃ©e et au dÃ©but de la forme
    :return: Le drapeau est tracÃ© sur la droite de la tortue et elle revient au dÃ©part
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
    :param width: La tortue est initialisÃ©e et au dÃ©but de la forme
    :return: Le drapeau est tracÃ© sur la droite de la tortue et elle revient au dÃ©part
    """
    three_color_flag(width, "black", "yellow", "red")


def french_flag(width):
    """
    Trace un drapeau franÃ§ais
    :param width: largeur
    :return: drapeau franÃ§ais
    """
    three_color_flag(width, "blue", "white", "red")


def horizontal_flag(width, color1, color2, color3):
    """
    RÃ©alisation d'un drapeau horizontal
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
    Ã©toile jaune
    :param width: largeur
    :return: Ã©toile jaune
    """
    tortue.color("yellow")
    tortue.pendown()
    tortue.begin_fill()
    for _ in range(5):
        tortue.forward(int(width / 3))
        tortue.right(144)
    tortue.end_fill()
    tortue.penup()


def european_flag(width):
    """
    drapeau europÃ©en
    :param width: largeur
    :return: drapeau europÃ©en
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

for i in range(3):  # Les 3 drapeaux belges
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
