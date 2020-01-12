def plus_frequent(l):
    """
    pre: liste
    post: element le plus fréquent
    """
    dic = {}
    for i in range(len(l)):
        try:
            dic[l[i]] = (dic[l[i]][0] + 1, dic[l[i]][1])
        except:
            dic[l[i]] = (1, i)
    print(dic)
    occurency = []
    for key in dic:
        occurency.append((dic[key], key))
    occurency.sort(reverse=True)
    print(occurency)
    if occurency[0][0][1] > occurency[1][0][1]:
        return occurency[1][1]
    return occurency[0][1]


def rainfall(l):
    """
    pre: liste de nombre, contient un 9999 qui stop
    post: retourne la moyenne des éléments, négatif = 0
    """
    for i in range(len(l)):
        if l[i] == 9999:
            l = l[:i]
            break

    tot = 0
    elem = 0
    for number in l:
        if number < 0:
            number = 0
        tot += number
        elem += 1

    return tot / elem


def load_matrix(filename):
    """
    pre: fichier
    post: une matrice, retourne None en cas d'erreur
    Flemme de faire les erreurs, il faut mettre des try .. except partout
    """
    with open(filename, "r") as file:
        instr = file.readlines()
        for i in range(len(instr)):
            instr[i] = instr[i].rstrip()
            if i > 1:
                instr[i] = instr[i].split(" ")
                instr[i][0] = instr[i][0].split(",")

    m, n = int(instr[0]), int(instr[1])
    instr = instr[2:]

    matrix = []
    for _ in range(m):
        temp = []
        for _ in range(n):
            temp.append(0.0)
        matrix.append(temp)

    for j in range(len(instr)):
        value = float(instr[j][1])
        x, y = int(instr[j][0][0]), int(instr[j][0][1])
        matrix[x][y] = value


class Client:
    """
    Un client. Chaque client a un nom d'utilisateur (supposé unique,
    par exemple adresse email) et un code pin qui est stocké comme un entier.
    """

    def __init__(self, name, pin):
        self.userName = name
        self.pin = pin

    def getUserName(self):
        return self.userName

    def getPin(self):
        return self.pin

    def setPin(self, pin):
        self.pin = pin

    def __str__(self):
        return self.userName + "(" + str(self.pin) + ")"


class ClientList:
    """Une liste de clients"""

    # un noeud de la liste
    class Node:
        def __init__(self, client, prev):
            self.data = client
            self.link = prev

    def __init__(self):
        self.last = None

    def __str__(self):
        pass

    def update(self, name, pin):
        """
        pre: name != None, la liste contient au plus un élément dont le username
             est `name`.
        post: Si un client dont le username est name est déjà présent, met à jour
              son code pin, sinon ajoute à la liste un nouveau client ayant `name`
              comme username et `pin` comme code pin.
        """
        curr, prev = self.last, None
        while curr != None:
            if curr.data.getUserName() == name:
                curr.data.setPin(pin)
                return curr.data
            curr, prev = curr.link, curr

        node = self.Node(Client(name, pin), None)
        try:
            prev.link = node
        except:
            self.last = node
        return node.data
