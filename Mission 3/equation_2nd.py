def racine_carree(a):
    pass


def rho(a, b, c):
    return b ** 2 - 4 * a * c


def n_solutions(a, b, c):
    if rho(a, b, c) == 0:
        return 1
    elif rho(a, b, c) < 0:
        return 0
    elif rho(a, b, c) > 0:
        return 2


def solution(a, b, c):
    if n_solutions(a, b, c) == 1:
        return - b / (2 * a)
    elif n_solutions(a, b, c) == 2:
        s1 = (-b + racine_carree(rho(a, b, c))) / (2 * a)
        s2 = (-b - racine_carree(rho(a, b, c))) / (2 * a)
        if s1 < s2:
            return s1
        return s2
