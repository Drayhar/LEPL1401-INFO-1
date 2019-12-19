# Recherche des racines d'une équation diophantienne x^a + y^b = z^c
# Vincent Bauffe, octobre 2019

#Cette fonction vérifie qu'il n'y ai pas de diviseurs commun, et retourne True dans ce cas
def diviseur(m, n, o):
    list = []
    for i in range(2, m + 1):
        if m % i == 0:
            list.append(i)
    for j in range(2, n + 1):
        if n % j == 0:
            list.append(j)
    for k in range(2, o + 1):
        if o % k == 0:
            list.append(k)
    global result
    result = False
    for r in range(max):
        if list.count(r) > 2:
            result = False
            break
        else:
            result = True

solutions = 0
a = int(input("Entrez la valeur de l'exposant a : ")) #Demande toutes les variables à l'utilisateur
b = int(input("Entrez la valeur de l'exposant b : "))
c = int(input("Entrez la valeur de l'exposant c : "))
max = int(input("Entrez la valeur maximale pour x, y et z : "))

for x in range(1,max): #Teste les différentes racines
    for y in range(1,max):
        for z in range(1, max):
            if x**a + y**b == z**c:
                diviseur(x, y, z)
                if result == True:
                    print("x =", x, " y =", y, "z =", z)
                    solutions += 1

if solutions == 0: #Impression du nombre de solutions trouvées
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees")