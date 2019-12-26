def get_country(l, name):
    for dic in l:
        if dic["City"] == name:
            return dic["Country"]
    return False
