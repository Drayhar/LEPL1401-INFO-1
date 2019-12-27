def count(events, i, j):
    coordinate = (i, j)
    sum = 0
    for i in events:
        if i == coordinate:
            sum += 1
    return sum
