def merge(first_list, second_list):
    third_list = first_list + second_list
    if first_list == [] or second_list == []:
        return first_list
    x = third_list[0][1]
    for _ in range(len(third_list) + 1):
        for i in range(1, len(third_list)):
            if third_list[i][1] < x:
                third_list[i - 1], third_list[i] = third_list[i], third_list[i - 1]
            x = third_list[i][1]
    return third_list
