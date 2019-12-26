def line_count(filename):
    sum = 0
    with open(filename, "r") as file:
        for _ in file:
            sum += 1
    return sum


def char_count(filename):
    sum = 0
    file = open(filename, "r")
    for _ in file.read():
        sum += 1
    file.close()
    return sum


def space(filename, n):
    file = open(filename, "w")
    for _ in range(n):
        file.write(" ")
    file.close()


def capitalize(filename_in, filename_out):
    file_in = open(filename_in, "r")
    file_out = open(filename_out, "w")
    for char in file_in.read():
        file_out.write(char.upper())
