class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def opposite(self):
        return Pair(-self.a, -self.b)
