from graphics import *  # un bibliothÃ¨que pour dessiner des figures simple sur un plan XY
import math  # nous avoins besoin des fonctions cos et sin pour notre calcul de la position d'un point
import Robot

class XYRobot(Robot.Robot):

    def __init__(self, n):
        super().__init__(n)
        self.__win = GraphWin()  # fenÃªtre graphique sur le chemin du robot sera tracÃ©

    def __drawFrom(self, oldx, oldy):
        line = Line(Point(oldx, oldy), Point(self.getx(), self.gety()))
        line.draw(self.__win)

    def __move(self, distance, sense):
        """ mÃ©thode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  il avance de distance pixels
            si sense = -1 il recule de distance pixels
        """
        oldx = self.getx()
        oldy = self.gety()
        orientationx = math.cos(self.getanglerad())
        orientationy = math.sin(self.getanglerad())
        self.setx(oldx + orientationx * distance * sense)
        self.sety(oldy + orientationy * distance * sense)
        self.__drawFrom(oldx, oldy)

    def __turn(self, direction):
        """ mÃ©thode auxiliaire pour les mÃ©thodes turnright() et turnleft()
            si direction = 1 elle change l'angle du robot de 90 degrÃ©s vers la droite (dans le sens des aiguilles d'une montre)
            si direction = -1 elle change l'angle du robot de 90 degrÃ©s vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.angle = self.angle + direction * math.pi / 2

    def moveforward(self, distance, history=True):
        """ fait avancer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance, 1)
        if history:
            self.history.append(("forward", distance))

    def movebackward(self, distance, history=True):
        """ fait reculer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance, -1)
        if history:
            self.history.append(("backward", -distance))

    def turnright(self, history=True):
        """ fait tourner le robot de 90 degrÃ©s vers la droite (dans le sens des aiguilles d'une montre)
        """
        self.__turn(1)
        if history:
            self.history.append(("right", 90))

    def turnleft(self, history=True):
        """ fait tourner le robot de 90 degrÃ©s vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(-1)
        if history:
            self.history.append(("left", -90))

    def unplay(self):
        self.history.reverse()
        for instruction in self.history:
            if instruction[0] == "forward":
                self.movebackward(instruction[1], False)
            elif instruction[0] == "backward":
                self.moveforward(instruction[1], False)
            elif instruction[0] == "right":
                self.turnleft(False)
            elif instruction[0] == "left":
                self.turnright(False)
        self.history = []


# Exemple d'utilisation de cette classe (il suffit d'exÃ©cuter ce fichier)

r2d2 = XYRobot("R2-D2")

# first move to position (100,100) facing East, to be more or less in the center of the window
print(r2d2)
r2d2.moveforward(100)
r2d2.turnright()
r2d2.moveforward(100)
r2d2.turnleft()

print(r2d2)
# R2-D2@(100, 100) angle: 0.0
r2d2.moveforward(50)
r2d2.turnleft()
print(r2d2)
# R2-D2@(150, 100) angle: 270.0
r2d2.moveforward(50)
r2d2.turnleft()
print(r2d2)
# R2-D2@(150.0, 50.0) angle: 180.0
r2d2.moveforward(50)
r2d2.turnleft()
print(r2d2)
# R2-D2@(100.0, 50.0) angle: 90.0
r2d2.moveforward(50)
print(r2d2)
# R2-D2@(100, 100) angle: 90.0
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
print(r2d2.getHistory())
r2d2.unplay()
print(r2d2)
