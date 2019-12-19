def extract(code):
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


# print(treatment("number number vowel-up vowel-low vowel-low vowel-low consonant-up number number number"))

def merge(first_list, second_list):
    # ['name', time]
    third_list = first_list + second_list
    print(third_list)
    x = third_list[0][1]
    for j in range(len(third_list) + 1):
        for i in range(1, len(third_list)):
            if third_list[i][1] < x:
                third_list[i - 1], third_list[i] = third_list[i], third_list[i - 1]
            x = third_list[i][1]
    print(third_list)
    return third_list


def house_designation(student_qualities):
    house = [[0, "Gryffindor"], [0, "Ravenclaw"], [0, "Hufflepuff"], [0, "Slytherin"]]
    knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
                 ['Ravenclaw', ['smart', 'wise', 'curious']],
                 ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
                 ['Slytherin', ['cunning', 'wily', 'malignant']]]
    new_list = []
    for i in range(4):
        for j in student_qualities:
            if j in knowledge[i][1]:
                house[i][0] += 1
    for m in range(3):
        for n in range(3):
            if house[n][0] < house[n + 1][0]:
                house[n], house[n + 1] = house[n + 1], house[n]
    for k in range(4):
        new_list.append(house[k][1])
    print(new_list)
    print(house)
    string = " ".join(new_list)
    print(string)
    return string


# house_designation(['smart', 'wise', 'bold', 'brave', 'hard-working', 'loyal', 'wily', 'malignant', 'curious'])

def search_time(l, t):
    """
    pre :  une liste d'événements l, un temps t
    post : l'index du premier élément dans l supérieur où égal à t; len(l) si un tel élément n'existe pas
    """


def absolute(v1, v2):
    """
    pre  : v1 et v2 deux nombres
    post : la fonction retourne |v1-v2|
    """


def euclidian_distance(c1, c2):
    """
    pre  : deux coordonnées c1=(x1,y1) et c2=(x2,y2)
    post : la fonction retourne la distance euclidienne entre c1 et c2
    """


def matrix_for_traces(l, theta_1, theta_2):
    """
    :param l: Liste de coordonnées [(temps, (x, y))]
    :param theta_1: ecart de temps
    :param theta_2: ecart de distance
    :return:
    """
    matrix = []
    for i in range(len(l)):
        for j in range(len(l)):
            temp = []
            for k in range(len(l[i])):
                for m in range(len(l[j])):
                    if absolute(l[i][k][0], l[j][m][0]) < theta_1 and euclidian_distance(l[i][k][1], l[j][m][1]) < theta_2 :
                        temp.append(1)
                    else:
                        temp.append(0)
            matrix.append(temp)
    return matrix



trace1 = [(1.0, (10.10, 20.0)), (3.0, (10.50, 20.30)), (5.0, (11.0, 21))]
trace2 = [(1.0, (15.00, 15.0)), (2.0, (12.00, 17.00)), (3.0, (10.50, 20)), (4.0, (12.0, 21.0))]
trace3 = [(1.0, (15.00, 15.0)), (3.0, (16.0, 21.0)), (5.0, (20.0, 21.0))]

#[1 1 0]
#[1 1 1]
#[0 1 1]

# print(matrix_for_traces([trace1,trace2,trace3],0.0,1.0))

def solution(a, b, c):
    """
    pre:  a, b et c sont 3 nombres réels
    post: la valeur de retour de cette fonction dépend du nombre
          de solutions de l'équation ax^2 + bx + c = 0.
    - 0 solution: retourne la liste vide
    - 1 solution: retourne une liste contenant la solution de l'équation
    - 2 solutions: retourne une liste contenant les deux solutions,
                  la plus petite solution en première place
    """


def solveur(list):
    matrix = [solution(i[0], i[1], i[2]) for i in list]
    return matrix


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

def create_dict_max(l):
    dict = {}
    for i in range(len(l)):
        dict[l[i][0]] = []
    for j in range(len(l)):
        dict[l[j][0]].append(l[j][1])
    for k in dict:
        dict[k] = max(dict[k])
    return dict


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
    return dictionary[word]


def get_country(l, name):
    for dic in l:
        if dic["City"] == name:
            return dic["Country"]
    return False


def table(filename_in, filename_out, width):
    with open(filename_in, "r") as file:
        global ville
        ville = file.readlines()
        for i in range(len(ville)):
            ville[i].rstrip("\n")
            if len(ville[i]) < width:
                ville[i] = ville[i] + " " * (width - len(ville[i]))
            elif len(ville[i]) > width:
                ville[i] = ville[i][:width]
    with open(filename_out, "w") as file:
        w = "-" * (width + 2)
        print = "+{0}+\n".format(w)
        for city in ville:
            print += "| {0} |\n".format(city)
        print += "+{0}+".format(w)
        file.writelines(print)

def write(letter_template, name):
    with open(letter_template, "r") as file:
        msg_list = file.read().split(" ")
        for i in range(len(msg_list)):
            if msg_list[i] == "#":
                msg_list[i] = "{0}"
        global msg_string
        msg_string = " ".join(msg_list)
        msg_string.format(name)
    with open(letter_template, "w") as file:
        file.write(msg_string)


def save_data(filename, life, mana, position_x, position_y):
    with open(filename, "w") as file:
        line = " ".join([str(life), str(mana), str(position_x), str(position_y)])
        file.writelines([str(life), "\n", str(mana), "\n", str(position_x), "\n", str(position_y)])


def load_data(filename):
    with open(filename, "r") as file:
        list = file.read().split("\n")
        for i in range(len(list)):
            list[i] = int(list[i])
        return (list[0], list[1], list[2], list[3])


def referee(score_file):
    with open(score_file, "r") as file:
        wholeList = ['A\n', 'B\n', 'A 10\n', 'B 10\n', 'A 10\n', 'A 10\n', 'B 10\n', 'A 10\n', 'A 10\n',
                     'B 150\n']  # file.readlines()
        team1, team2 = wholeList[0].rstrip("\n"), wholeList[1].rstrip("\n")
        points = wholeList[2:]
        print(points)
        for i in range(len(points)):
            points[i] = points[i].rstrip("\n")
            points[i] = points[i].split(" ")
        j = 0
        team1S = 0
        team2S = 0
        while True:
            if points[j][0] == team1:
                team1S += int(points[j][1])
                if team1S >= 150:
                    return team1
            elif points[j][0] == team2:
                team2S += int(points[j][1])
                if team2S >= 150:
                    return team2


def translate(data):
    code = ""
    for letter in data:
        try:
            code += morse[letter]
        except TypeError:
            return TypeError
    return code

def get_max(filename):
    """
    pre:    filename est une chaîne de caractères
    post:   Renvoie le plus grand nombre réel >= 0 trouvé dans le fichier de nom
            filename.
            Les lignes ne représentant pas un seul nombre réel >= 0 sont ignorées.
            Si le fichier n'existe pas ou si une erreur d'entrée/sortie survient,
            la fonction renvoie la valeur -1, et imprime un message d'erreur.
            Si le fichier ne contient aucune ligne valide, renvoie
            la valeur -1.

            Par exemple, la méthode retourne 10.0 pour le fichier de contenu suivant:
            0.345.67
            hello
            -543.0
            500.0 1000.0 2000.0
            10.0
            3.1416
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            try:
                temp = lines[i].split(" ")
                lines[i] = lines[i][0]
            except:
                pass


print("test")

#test