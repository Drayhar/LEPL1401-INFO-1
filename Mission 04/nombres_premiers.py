def primes(max):
    list = []
    if max <= 1:
        return list
    if max == 2:
        return [2]
    prime = [True for i in range(max + 1)]
    p = 2
    while (p * p <= max):
        if (prime[p] == True):
            for i in range(p * 2, max + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(max + 1):
        if prime[p]:
            list.append(p)
    return list
