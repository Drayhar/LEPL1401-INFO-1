# Recherche des racines d'une Ã©quation diophantienne x^a + y^b = z^c
# Vincent Bauffe, octobre 2019

# Cette fonction vÃ©rifie qu'il n'y ai pas de diviseurs commun, et retourne True dans ce cas


def diviseur(m, n, o):
    list = []
    for i in range(2, m):
        if m % i == 0:
            list.append(i)
    for j in range(2, m):
        if n % j == 0:
            list.append(j)
    for k in range(2, m):
        if o % k == 0:
            list.append(k)
    global result
    result = False
    for r in range(100):
        if list.count(r) > 1:
            result = False
            break
        else:
            result = True
    return result


solutions = 0
# Demande toutes les variables Ã  l'utilisateur
a = int(input("Entrez la valeur de l'exposant a : "))
b = int(input("Entrez la valeur de l'exposant b : "))
c = int(input("Entrez la valeur de l'exposant c : "))
max = int(input("Entrez la valeur maximale pour x, y et z : "))

for x in range(1, max):  # Teste les diffÃ©rentes racines
    for y in range(1, max):
        for z in range(1, max):
            if x**a + y**b == z**c:
                diviseur(x, y, z)
                if result == True:
                    print("x =", x, " y =", y, "z =", z)
                    solutions += 1

if solutions == 0:  # Impression du nombre de solutions trouvÃ©es
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees")
