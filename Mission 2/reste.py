a, b = 0, 0
rest = 0
if b == 0:
    rest = None
else:
    for i in range(1, a + b):
        if (a - i) / b == a // b:
            rest = i
