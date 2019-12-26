class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __eq__(self, p):
        if p == None:
            return False
        elif p.a == self.a and p.b == self.b:
            return True
        else:
            return False
