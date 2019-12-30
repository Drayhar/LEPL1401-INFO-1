matrix = [[31, 24, 55],
          [-61, -37, 44],
          [-88, 16, -13],
          [-14, -78, 62],
          [53, -19, 56],
          [73, 16, -77]]

sum_even = 0
m, n = len(matrix), len(matrix[0])
i, j = 0, 0
while i < m:
    j = 0
    while j < n:
        elem = matrix[i][j]
        if elem % 2 == 0:
            sum_even += elem
        j += 1
    i += 1
