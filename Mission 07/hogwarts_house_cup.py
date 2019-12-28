students = {'gryffindor': ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville'],
            'ravenclaw': ['Cho', 'Luna', 'Sybill', 'Marcus', 'Marietta', 'Terry', 'Penelope'],
            'hufflepuff': ['Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton', 'Justin'],
            'slytherin': ['Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']}


def winning_house(scroll):
    with open(scroll, "r") as file:
        listt = file.readlines()
        dictt = {}
        for i in range(len(listt)):
            listt[i] = listt[i].rstrip("\n").split(" ")
            listt[i][1] = int(listt[i][1])
            try:
                dictt[listt[i][0]] += listt[i][1]
            except:
                dictt[listt[i][0]] = listt[i][1]

        score = {}
        for house in students:
            points = 0
            for name in students[house]:
                try:
                    points += dictt[name]
                except:
                    pass
            score[house] = points

        gagnant = []
        for maison in score:
            gagnant.append((score[maison], maison))
        gagnant.sort(reverse=True)

        print(listt)
        print(dictt)
        print(score)
        print(gagnant)

        if gagnant[0][0] > gagnant[1][0]:
            return gagnant[0][1]
        else:
            return [gagnant[1][1], gagnant[0][1]]
