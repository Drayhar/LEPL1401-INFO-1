words = ["while", "the", "congress", "of", "the", "republic", "endlessly", "debates", "this", "alarming", "chain",
         "of", "events", "the", "supreme", "chancellor", "has", "secretly", "dispatched", "two", "jedi", "knights"]


def topk_words(words, k):
    dic = {}
    for word in words:
        try:
            dic[word] += 1
        except:
            dic[word] = 1

    listt = []
    for key in dic:
        listt.append((dic[key], key))
    listt = sorted(listt, reverse=True)

    maxi = listt[0][0]
    stop = maxi - k
    for i in range(len(listt)):
        if k >= maxi:
            return listt
        elif listt[i][0] <= stop:
            return listt[:i]


print(topk_words(words, 4))
