from math import sqrt


def search_time(l, t):
    pass


def absolute(v1, v2):
    return abs(v1-v2)


def euclidian_distance(c1, c2):
    return sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2)


def matrix_for_traces(l, theta_1, theta_2):
    """
    Pre: liste de traces
    Post: matrice, si matrice[i][j] == 1, les traces i et j se croisent
    """
    matrice = []

    for i in range(len(l)):  # Trace principale
        trace_main = l[i]
        list_temp = []

        for j in range(len(l)):  # Trace secondaire
            trace_second = l[j]
            list_temp.append(0)
            for k in range(len(l[i])):  # Coord Main
                coord_main_n = l[i][k]
                for m in range(len(l[j])):  # Coord seconde
                    coord_second_n = l[j][m]

                    # condition ok
                    if absolute(coord_main_n[0], coord_second_n[0]) <= theta_1 and euclidian_distance(coord_main_n[1], coord_second_n[1]) <= theta_2:
                        list_temp[j] = 1
                        if list_temp[j] == 1:
                            break
                    if list_temp[j] == 1:
                        break
                if list_temp[j] == 1:
                    break

        matrice.append(list_temp)
    return matrice


trace1 = [(1.0, (10.10, 20.0)), (3.0, (10.50, 20.30)), (5.0, (11.0, 21))]
trace2 = [(1.0, (15.00, 15.0)), (2.0, (12.00, 17.00)),
          (3.0, (10.50, 20)), (4.0, (12.0, 21.0))]
trace3 = [(1.0, (15.00, 15.0)), (3.0, (16.0, 21.0)), (5.0, (20.0, 21.0))]
print(matrix_for_traces([trace1, trace2, trace3], 0.0, 1.0))

trace4 = [(1.0, (10.1, 20.0)), (3.0, (10.5, 20.3)), (5.0, (11.0, 21))]
trace5 = [(1.0, (15.0, 15.0)), (2.0, (12.0, 17.0)),
          (3.0, (10.5, 20)), (4.0, (12.0, 21.0))]

print(matrix_for_traces([trace4, trace5], 0, 0))
