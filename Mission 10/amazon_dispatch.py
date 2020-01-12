class Command:
    nbre_commande = 0
    price_tot = 0

    def __init__(self, id_buyer, id_item, quantity, price):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity = quantity
        self.price = price
        self.tot = self.quantity * self.price
        Command.nbre_commande += 1
        Command.price_tot += self.tot

    def get_price(self):
        return self.tot

    def __str__(self):
        return "{}, {} : {} * {} = {}".format(self.id_buyer, self.id_item, self.price, self.quantity, self.tot)

    @classmethod
    def get_number_total_command(cls):
        return Command.nbre_commande

    @classmethod
    def get_total_price(cls):
        return Command.price_tot
