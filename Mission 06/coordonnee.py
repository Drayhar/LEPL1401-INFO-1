def write_coordinates(filename, l):
    with open(filename, "w") as file:
        list = []
        length = len(l)
        x = 0
        for i in l:
            temp = str(i[0]) + "," + str(i[1])
            x += 1
            if x != length:
                temp += "\n"
            list.append(temp)
            print(list)
        file.writelines(list)


def read_coordinates(filename):
    with open(filename, "r") as file:
        big_list = []
        for line in file:
            line = line.strip("\n")
            list = line.split(",")
            temp = (float(list[0]), float(list[1]))
            big_list.append(temp)
            print(temp)
        return big_list
