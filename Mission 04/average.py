def average(list):
    if list == []:
        return None
    somme = 0
    nbre = 0
    for i in list:
        if type(i) != str:
            somme += i
            nbre += 1
    mean = somme / nbre
    return mean
