class Employe:

    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def augmente(self, percent):
        self.salaire += (percent / 100) * self.salaire

    def __str__(self):
        return "{0} : {1}".format(self.nom, self.salaire)
