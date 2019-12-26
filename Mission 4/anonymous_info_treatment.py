def treatment(data):
    list = data.split(" ")
    new_list = []
    print(list)
    j = 0
    while j < len(list) - 1:
        if list[j] != list[j + 1]:
            new_list.append(list[j] + "*1")
            j += 1
        else:
            iteration = 1
            while list[j] == list[j + iteration]:
                iteration += 1
                print("tutu")
                if j + 1 + iteration >= len(list):
                    break
            new_list.append(list[j] + "*{0}".format(iteration))
            j += iteration
    print(new_list)
    string = " ".join(new_list)
    return string
