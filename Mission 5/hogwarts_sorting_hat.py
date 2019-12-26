def house_designation(student_qualities):
    house = [[0, "Gryffindor"], [0, "Ravenclaw"],
             [0, "Hufflepuff"], [0, "Slytherin"]]
    knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
                 ['Ravenclaw', ['smart', 'wise', 'curious']],
                 ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
                 ['Slytherin', ['cunning', 'wily', 'malignant']]]
    new_list = []
    for i in range(4):
        for j in student_qualities:
            if j in knowledge[i][1]:
                house[i][0] += 1
    for _ in range(3):
        for n in range(3):
            if house[n][0] < house[n + 1][0]:
                house[n], house[n + 1] = house[n + 1], house[n]
    for k in range(4):
        new_list.append(house[k][1])
    print(new_list)
    print(house)
    string = " ".join(new_list)
    print(string)
    return new_list
