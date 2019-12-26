def triangle(n):
    big_list = []
    list = []
    for i in range(n + 1):
        for j in range(0, i + 1):
            list.append(j)
            print(list)
        big_list.append(list)
        list = []
    return big_list
