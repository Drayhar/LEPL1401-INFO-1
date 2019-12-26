a = 1
c = 0

while a <= 10:
    b = a ** 2
    c += b
    d = int((a * (a + 1) * (2 * a + 1)) / 6)
    print(a, "\t", b, "\t", c, "\t", d)
    a += 1
