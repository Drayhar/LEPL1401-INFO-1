def fibonacci(n):
    if n <= 1:
        return n
    f1 = 0
    f2 = 1
    fn = 0
    for _ in range(1, n):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn
