def create_dictionary(filename):
    with open(filename, "r") as file:
        string = file.read()
        list = string.split(" ")
        if string == "":
            dictionary = {}
            return dictionary
        else:
            dictionary = {}
            for i in list:
                dictionary[i] = 0
            for j in list:
                dictionary[j] += 1
    return dictionary


def occ(dictionary, word):
    try:
        return dictionary[word]
    except:
        return 0
