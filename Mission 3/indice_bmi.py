def quetelet(height, weight):
    a = "thin"
    b = "normal"
    c = "overweight"
    d = "obese"
    indice = int(weight / height ** 2)
    if indice < 20:
        return a
    elif 20 <= indice <= 25:
        return b
    elif 25 < indice <= 30:
        return c
    elif indice > 30:
        return d
