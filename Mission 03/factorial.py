def fact(n):
    """
    :param n: -
    :return: la factorielle de 'n'
    """
    fac = 1
    for i in range(n):
        fac = fac * (n - i)
    return fac
