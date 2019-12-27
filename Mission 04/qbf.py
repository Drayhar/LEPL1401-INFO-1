def positions(p, s):
    list = []
    s = s.lower()
    p = p.lower()
    for i in range(len(s) - 1):
        if (p[0] == s[i] or p[0] == "?") and (p[1] == s[i + 1] or p[1] == "?"):
            list.append(i)
    return list
