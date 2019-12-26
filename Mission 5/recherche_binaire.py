def binary_search(course, list_of_courses):
    #[('LINFO1101', ['Jean', 'Pierre']),('LINFO1110', ['Jean']), ('LINFO1111', ['Jean']), ('LINFO1112', ['Jacques', 'Pierre']), ('LINFO1113', ['Pierre'])]
    student = []
    first = 0
    last = len(list_of_courses)-1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if list_of_courses[middle][0] == course:
            student = list_of_courses[middle][1]
            found = True
        else:
            if course < list_of_courses[middle][0]:
                last = middle - 1
            else:
                first = middle + 1

    return student
