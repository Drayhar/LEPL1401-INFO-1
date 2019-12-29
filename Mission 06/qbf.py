def get_max(filename):
    try:
        file = open(filename, "r")
        listt = file.readlines()
        empty = True
        max = 0
        for i in range(len(listt)):
            listt[i] = listt[i].rstrip("\n")
            try:
                temp = float(listt[i])
                empty = False
                if temp > max:
                    max = temp
            except:
                pass
        if empty or max == 0:
            return -1
        else:
            return max
    except:
        print("Error while handling file")
        return -1


print(get_max("scratch"))
