n = 0

for i in range(1, n + 1):
    div = 0
    for k in range(1, i):
        if i % k == 0:
            div += 1
    print(i, ":", div)
