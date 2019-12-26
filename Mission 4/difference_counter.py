def diff_count(lst):
    different = 0
    seen = []
    for i in lst:
        if i not in seen:
            different += 1
        seen.append(i)
    return different
