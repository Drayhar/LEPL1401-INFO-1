class Ticket:

    __prochain_numero = 1  # variable de classe pour générer le numéro du ticket

    def __init__(self):
        self.__numero = Ticket.__prochain_numero
        Ticket.__prochain_numero += 1

    def numero(self):
        return self.__numero
