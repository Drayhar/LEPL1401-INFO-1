class Item:

    def __init__(self, author, title, serial):
        """
        Méthode d'initialisation.
        @pre  author et title sont des valeurs de type String
              serial est un entier > 0
        @post Une instance de la classe est créée, et représente un objet ayant
              comme auteur author, comme titre title et comme numéro de série serial
        """
        self.author = author
        self.title = title
        self.serial = serial

    def __str__(self):
        """
        Méthode de conversion en string.
        @pre  -
        @post le string retourné contient une représentation de cet objet sous la
              forme: [num série] Auteur, Titre
        """
        return "[{}] {}, {}".format(self.serial, self.author, self.title)


class CD(Item):

    __serial = 100000

    def __init__(self, author, title, length):
        super().__init__(author, title, CD.__serial)
        CD.__serial += 1
        self.length = length

    def __str__(self):
        return "[{0}] {1}, {2} ({3} s)".format(self.serial, self.author, self.title, self.length)


disque = CD("Moi", "L'amour", 350)
print(disque)
