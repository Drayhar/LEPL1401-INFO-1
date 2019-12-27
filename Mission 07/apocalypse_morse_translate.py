morse = {}


def translate(data):
    code = ""
    for letter in data:
        try:
            code += morse[letter]
        except (TypeError, KeyError):
            raise TypeError
    return code
