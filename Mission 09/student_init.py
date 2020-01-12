class Student:
    nbr = 0

    def __init__(self, firstname, surname, birthday, email):
        self.firstname = firstname
        self.surname = surname
        self.date = birthday
        self.email = email
        self.nbr = Student.nbr
        Student.nbr += 1

    def __str__(self):
        msg = "Student number {0}: {1} {2} born the {3}, can be reached at {4}".format(
            self.nbr, self.firstname, self.surname, self.date, self.email)
        return msg


stu = Student("Vincent", "Bauffe", "20102001", "oui")
print(stu)
