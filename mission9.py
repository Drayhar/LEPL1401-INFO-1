class Article:
    __taux_tva = 0.21  # TVA a 21%

    def __init__(self, d, p):
        """
        Cree un article avec description d et prix p.
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        Retourne la description de cet article.
        """
        return self.__description

    def prix(self):
        """
        Retourne le prix (HTVA) de cet article.
        """
        return self.__prix

    def taux_tva(self):
        """
        Retourne le taux de TVA (même valeur pour chaque article)
        """
        return self.__taux_tva

    def tva(self):
        """
        Retourne la TVA sur cet article
        """
        return self.prix() * self.taux_tva()

    def prix_tvac(self):
        """
        Retourne le prix de l'article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        Retourne un texte decrivant cet article, au format: "{description}: {prix}"
        """
        # WRONG:
        #   return "{0}: {1:.2f}".format(self.get_description, self.get_prix())
        # RIGHT:
        return "{0}: {1:.2f}".format(self.description(), self.prix())


class Facture:

    def __init__(self, description, articles, numero):
        """
        Crée une facture avec une description (titre) et un liste d'articles.
        """
        self.__reference = description
        self.__articles = articles
        self.__numero = numero

    def description(self):
        """
        Retourne la description de cette facture.
        """
        return self.__reference

    def articles(self):
        """
        Retourne la liste des articles de cette facture.
        """
        return self.__articles

    def __str__(self):
        """
        Retourne la représentation string d'une facture, à imprimer avec la méthode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles():
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Facture No {0} ".format(self.__numero) + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "prix HTVA", "TVA", "prix TVAC")
        e += self.barre_str()
        return e

    def entete_livraison(self):
        e = "Livraison - Facture No {0} ".format(self.__numero) + " : " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "poids/pce", "nombre", "poids")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string représentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
        Retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(),
                                                                         art.prix_tvac())

    def article_livraison(self, art):
        return "| {0:40} | {1:8.3f}kg | {2:10.0f} | {3:8.3f}kg |\n".format(art.p.description(), art.p.poids(), art.nombre(),
                                                                         art.p.poids() * art.nombre())

    def totaux_str(self, prix, tva):
        """
        Retourne un string représentant une ligne de facture avec les totaux prix et tva, à imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix + tva)
        b += self.barre_str()
        return b

    def totaux_livraison(self, nombre, poids):
        b = self.barre_str()
        b += "| {0:40} | {1:10} | {2:10.0f} | {3:8.3f}kg |\n".format("{0} articles".format(len(self.__articles)), "", nombre, poids)
        b += self.barre_str()
        return b

    # This method needs to be added during Etape 4 of the mission
    def nombre(self, pce):
        """
        Retourne le nombre d'exemplaires de la pièce pce dans la facture, en totalisant sur tous les articles qui concernent cette pièce.
        """
        sum = 0
        for art in self.articles():
            try:
                if art.p == pce.p:
                    sum += art.nombre()
            except:
                pass
        return sum


    # This method needs to be added during Etape 5 of the mission
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        s = self.entete_livraison()
        totalNombre = 0.0
        totalPoids = 0.0
        for art in self.articles():
            s += self.article_livraison(art)
            totalNombre = totalNombre + art.nombre()
            totalPoids = totalPoids + art.p.poids() * art.nombre()
        s += self.totaux_livraison(totalNombre, totalPoids)
        for art in self.articles():
            if art.p.fragile():
                s += "(!) *** livraison fragile ***"
                break
        return s

    def printLivraison(self):
        print(self.livraison_str())


class ArticleReparation(Article):

    def __init__(self, duree):
        #super().__init__(d, p)
        self.duree = duree

    def description(self):
        return "Réparation ({0} heures)".format(self.duree)

    def prix(self):
        return 20 + 35 * self.duree


class Piece:

    def __init__(self, d, p, po=0.0, s=False, t=False):
        self.__description = d
        self.__prix = p
        self.__poids = po
        self.__fragile = s
        self.__tva = t

    def description(self):
        return self.__description

    def prix(self):
        return self.__prix

    def poids(self):
        return self.__poids

    def fragile(self):
        return self.__fragile

    def tva_reduit(self):
        return self.__tva

    def __eq__(self, other):
        if self.__description == other.__description and self.__prix == other.__prix:
            return True
        return False


class ArticlePiece(Article):

    def __init__(self, q, p):
        self.__nombre = q
        self.p = p

    def nombre(self):
        return self.__nombre

    def description(self):
        return "{0} * {1} @ {2}".format(self.__nombre, self.p.description(), self.p.prix())

    def prix(self):
        return self.p.prix() * self.__nombre

    def tva(self):
        if self.p.tva_reduit():
            return self.prix() * 0.06
        return self.prix() * self.taux_tva()


class TestArticleInitial:
    articles = [Article("laptop 15\" 8GB RAM", 743.79),
                Article("installation windows", 66.11),
                Article("installation wifi", 45.22),
                Article("carte graphique", 119.49),
                ArticleReparation(0.75)
                ]

    @classmethod
    def run(cls):
        for art in cls.articles:
            print(art)


class TestFactureInitial:
    articles = [
                ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.10, True)),
                ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.10)),
                ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.10))
                ]

    @classmethod
    def run(cls):
        fac = Facture("PC Store - 22 novembre", cls.articles, 1)
        print(fac)
        fac.printLivraison()


if __name__ == "__main__":
    TestArticleInitial.run()

print("")

if __name__ == "__main__":
    TestFactureInitial.run()


