def create_dict_max(l):
    dict = {}
    for i in range(len(l)):
        dict[l[i][0]] = []
    for j in range(len(l)):
        dict[l[j][0]].append(l[j][1])
    for k in dict:
        dict[k] = max(dict[k])
    return dict
