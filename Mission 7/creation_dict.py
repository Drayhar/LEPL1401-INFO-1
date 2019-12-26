def create_dict(l):
    dict = {}
    for i in range(len(l)):
        dict[l[i][0]] = []
    for j in range(len(l)):
        dict[l[j][0]].append(l[j][1])
    return dict
