import math
from graphics import *

class Robot:

    def __init__(self, n):
        self.nom = n  # nom du robot
        self.x = 0  # position x du robot
        self.y = 0  # position y du robot
        self.angle = 0  # angle en degres radius
        self.history = []

    def __str__(self):
        """Imprime un string du type "R2-D2@(100,100) angle: 0.0" reprÃ©sentant les coordonnÃ©es position du robot."""
        return str(self.getnom()) + "@(" + str(round(self.getx())) + "," + str(round(self.gety())) + ") angle: " + str(
            self.getangle())

    def getnom(self):
        return self.nom

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getanglerad(self):
        """returns the angle in radials"""
        return self.angle

    def getangle(self):
        """returns the angle in degrees"""
        return (self.angle * 180 / math.pi) % 360

    def getHistory(self):
        return self.history

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def position(self):
        return (self.getx(), self.gety())
