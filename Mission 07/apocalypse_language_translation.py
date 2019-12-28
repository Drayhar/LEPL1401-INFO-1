lan = {'test': 'prueba', 'i': 'yo', 'you': 'te', 'elephant': 'elefante', 'this': 'esta',
       'is': 'es', 'a': 'un', 'shot': 'disparo', 'an': 'un', 'in': 'en', 'my': 'mi', 'pajama': 'pijama'}

data = "I shot an elephant in my pajama"


def translate(data, lan):
    listt = data.lower().split(" ")
    translate = []
    for i in range(len(listt)):
        try:
            translate.append(lan[listt[i]])
        except:
            translate.append(listt[i])
    return " ".join(translate) + " "


print(translate(data, lan))
