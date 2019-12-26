def sum(list):
    somme = 0
    for i in list:
        if type(i) == int or type(i) == float:
            somme += i
    return somme
