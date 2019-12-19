# from mission8 import Duree, Chanson, Album
#
# test_1 = Duree(0, 2, 0)
# test_2 = Duree(0, 0, 1)
#
# chanson_1 = Chanson("Puree", "Cool", test_1)
#
# album_1 = Album(0)
#
#
# assert test_1.toSecondes() == 120
# assert test_1.delta(test_2) == 119
# assert test_1.apres(test_2) == True
# assert test_2.apres(test_1) == False
# assert test_1.ajouter(test_2) == (0, 2, 1)
#
# assert album_1.add(chanson_1) == None
# assert album_1.state()


from mission9 import *

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