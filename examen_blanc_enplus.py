def mix(l):
    """
    pre: liste avec un nombre pair d'entiers
    post: [1, n, 2, n-1, ...]
    """
    length = len(l)
    new_list = []
    for i in range(int(length / 2)):
        new_list.append(l[i])
        new_list.append(l[length - 1 - i])
    return new_list


def combien(n):
    """
    pre: int
    post: nbre série d'entier qui s'addionnent pour arriver à n
    """
    occ = 0
    for i in range(0, n+1):
        sum = i
        j = 0
        while sum <= n:
            if sum == n:
                occ += 1
            j += 1
            sum += (i + j)
    return occ


def somme_des(n):
    """
    pre: int
    post: dic : clé = somme valeur possible, valeur = tuple qui s'addionnent pour donner e
    """
    dic = {}
    for j in range(1, n+1):
        for k in range(1, n+1):
            try:
                dic[j + k].append((j, k))
            except:
                dic[j + k] = [(j, k)]
    return dic


def acrostiche(file_name):
    """
    pre: nom du fichier
    post: string avec première lettre de chaque ligne
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except:
        return -1
    acro = ""
    for line in lines:
        for letter in line:
            if letter.isalpha():
                acro += letter
                break
    return acro


class SudokuPuzzle:
    def __init__(self, dimension):
        """
        Crée un SudokuPuzzle de dimension `dimension` avec tous les éléments initialisés à 0.
        """
        self.dimension = dimension
        self.carres = [[SudokuCarre(x, y, dimension)
                        for x in range(dimension)]
                       for y in range(dimension)]

    def get_carre(self, x, y):
        """
        Retourne le SudokuCarre qui se trouve à la position (x, y) dans ce Sudoku.
        """
        return self.carres[y][x]

    def get_carre_valeurs(self, x, y):
        carre = self.get_carre(x, y)
        occ = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                occ.append(carre.get_val(j, i))
        return occ

    def get_ligne(self, ligne):
        line_inside = ligne % self.dimension
        line_carre = ligne // self.dimension
        occ = []
        for square in range(self.dimension):
            temp = self.get_carre(square, line_carre)
            for value in range(self.dimension):
                occ.append(temp.get_val(value, line_inside))
        return occ

    def get_colonne(self, colonne):
        colonne_inside = colonne % self.dimension
        colonne_carre = colonne // self.dimension
        occ = []
        for square in range(self.dimension):
            temp = self.get_carre(colonne_carre, square)
            for value in range(self.dimension):
                occ.append(temp.get_val(colonne_inside, value))
        return occ

    def est_correcte(self):
        for line in range(self.dimension ** 2):
            temp = self.get_ligne(line)
            for value in range(self.dimension ** 2):
                if temp.count(value) > 1:
                    return False

        for colonne in range(self.dimension ** 2):
            temp = self.get_colonne(colonne)
            for value in range(self.dimension ** 2):
                if temp.count(value) > 1:
                    return False

        for x in range(self.dimension):
            for y in range(self.dimension):
                temp = self.get_carre_valeurs(x, y)
                if temp.count(value) > 1:
                    return False

        return True

    def __str__(self):
        """
        Retourne un texte permettant de représenter le Sudoku.
        """
        s = ""
        for y in range(len(self.carres)):
            for x in range(len(self.carres[y])):
                s += str(self.get_carre(x, y))
            s += "\n"
        return s


class SudokuCarre:

    def __init__(self, x, y, dimension):
        """
        Crée un SudokuCarre de taille `dimension` x `dimension`, avec toutes ses valeurs initialisées à 0.
        """
        self.xcoord_carre = x
        self.ycoord_carre = y
        self.cells = [[0 for x in range(dimension)]
                      for y in range(dimension)]

    def set_val(self, x, y, val):
        """
        Assigne une valeur `val` à la cellule se trouvant à la position (x, y) de ce carré.
        """
        self.cells[y][x] = val

    def get_val(self, x, y):
        """
        Retourne la valeur qui se trouve à la position (x, y) de ce carré.
        """
        return self.cells[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le contenu de ce carré.
        """
        s = "carré (" + str(self.xcoord_carre) + "," + \
            str(self.ycoord_carre) + ") : "
        s += str(self.cells)
        s += " "
        return s
