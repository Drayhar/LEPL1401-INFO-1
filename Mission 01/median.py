a, b, c = 53, 72, 35

if a <= b <= c or c <= b <= a:
    median = b
elif a <= c <= b or b <= c <= a:
    median = c
elif b <= a <= c or c <= a <= b:
    median = a
