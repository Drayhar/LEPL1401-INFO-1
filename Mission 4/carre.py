def carre(n):
    list = []
    big_list = []
    for j in range(n):
        for i in range(n):
            list.append(i + j * n)
        big_list.append(list)
        list = []
    return big_list
