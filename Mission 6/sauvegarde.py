def save_data(filename, life, mana, position_x, position_y):
    with open(filename, "w") as file:
        _ = " ".join(
            [str(life), str(mana), str(position_x), str(position_y)])
        file.writelines([str(life), "\n", str(mana), "\n",
                         str(position_x), "\n", str(position_y)])

#save_data("scratch", 1, 2, 3, 4)


def load_data(filename):
    with open(filename, "r") as file:
        list = file.read().split("\n")
        for i in range(len(list)):
            list[i] = int(list[i])
        return (list[0], list[1], list[2], list[3])
