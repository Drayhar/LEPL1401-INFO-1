a_list = []
x = a_list[0]
for j in range(len(a_list)):
    for i in range(1, len(a_list)):
        if a_list[i] < x:
            a_list[i], a_list[i-1] = a_list[i - 1], a_list[i]
        x = a_list[i]
sorted_list = a_list
