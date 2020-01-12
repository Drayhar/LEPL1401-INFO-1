class Student:

    def __init__(self, firstname, surname, mark):
        self.firstname = firstname
        self.surname = surname
        self.mark = mark


def marks_from_file(filename):
    students = []
    with open(filename, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n").split(" ")
        students.append(Student(lines[i][0], lines[i][1], int(lines[i][2])))

    return students
