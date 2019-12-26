s0 = 0
print(s0)
while s0 != 1:
    if s0 % 2 == 0:
        s0 = int(s0 / 2)
    elif s0 % 2 != 0:
        s0 = int(3 * s0 + 1)
    print(s0)
