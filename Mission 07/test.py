import search


assert search.create_index("test_exemple_1.txt") == {'lorem': {0: 1}, 'ipsum': {0: 1}, 'dolor': {0: 1, 3: 1}, 'sit': {0: 1}, 'amet': {0: 1}, 'consectetur': {0: 1}, 'adipiscing': {0: 1}, 'elit': {0: 1}, 'sed': {0: 1}, 'do': {0: 1}, 'eiusmod': {0: 1}, 'tempor': {0: 1}, 'incididunt': {1: 1}, 'ut': {1: 2, 2: 1}, 'labore': {1: 1}, 'et': {1: 1}, 'dolore': {1: 1, 3: 1}, 'magna': {1: 1}, 'aliqua': {1: 1}, 'enim': {1: 1}, 'ad': {1: 1}, 'minim': {1: 1}, 'veniam': {1: 1}, 'quis': {1: 1}, 'nostrud': {1: 1}, 'eercitation': {2: 1}, 'ullamco': {2: 1}, 'laboris': {2: 1}, 'nisi': {2: 1}, 'aliquip': {2: 1}, 'e': {
    2: 1}, 'ea': {2: 1}, 'commodo': {2: 1}, 'consequat': {2: 1}, 'duis': {2: 1}, 'aute': {2: 1}, 'irure': {2: 1}, 'in': {3: 2, 4: 1}, 'reprehenderit': {3: 1}, 'voluptate': {3: 1}, 'velit': {3: 1}, 'esse': {3: 1}, 'cillum': {3: 1}, 'eu': {3: 1}, 'fugiat': {3: 1}, 'nulla': {3: 1}, 'pariatur': {3: 1}, 'ecepteur': {4: 1}, 'sint': {4: 1}, 'occaecat': {4: 1}, 'cupidatat': {4: 1}, 'non': {4: 1}, 'proident': {4: 1}, 'sunt': {4: 1}, 'culpa': {4: 1}, 'qui': {4: 1}, 'officia': {4: 1}, 'deserunt': {4: 1}, 'mollit': {4: 1}, 'anim': {4: 1}, 'id': {4: 1}, 'est': {4: 1}, 'laborum': {4: 1}}, "Wrong index"
#assert search.readfile("text_exemple_2.txt") == ['Une garde au pneu genereuse', 'des surfaces lisses et un passage', 'interne des cables vous assurent', 'de rester en course et de limiter', 'les passages en zone techniques', 'meme dans les pires conditions'], "Error readfile"
assert search.get_words("Ce programme marche t il") == [
    'ce', 'programme', 'marche', 't', 'il'], "error get words"
assert search.get_lines(["des", "cables"], search.create_index(
    "test_exemple_2.txt")) == [2], "error get_lines"
