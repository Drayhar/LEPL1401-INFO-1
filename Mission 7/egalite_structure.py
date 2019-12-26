def equal(l, d):
    try:
        state = True
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] != 0:
                    if l[i][j] != d[(i, j)]:
                        state = False
    except:
        state = False
    return state
