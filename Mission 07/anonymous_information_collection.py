def extract(code):
    """
    Donne la nature de chaque élément d'une string
    """
    vowel_up = "AEIOUY"
    vowel_low = "aeiouy"
    consonant_up = "BCDFGHJKLMNPQRSTVWXZ"
    consonant_low = "bcdfghjklmnpqrstvwxz"
    number = "1234567890"
    answer = ""
    for i in code:
        if i in number:
            answer += "number"
        elif i in vowel_up:
            answer += "vowel-up"
        elif i in vowel_low:
            answer += "vowel-low"
        elif i in consonant_up:
            answer += "consonant-up"
        elif i in consonant_low:
            answer += "consonant-low"
        answer += " "
    return answer


def treatment(data):
    """
    Transforme une suite d'éléments en un pattern
    """
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


def collect(file):
    with open(file, "r") as filee:
        msg_list = filee.readlines()
        dic = {}
        for i in range(len(msg_list)):
            msg_list[i] = msg_list[i].rstrip("\n")
            data = extract(msg_list[i])
            occ = treatment(data)
            try:
                dic[occ] += 1
            except:
                dic[occ] = 1

    return dic
