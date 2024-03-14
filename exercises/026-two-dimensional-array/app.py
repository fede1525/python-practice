def two_dimensional_list(x, y):
    matrix = []

    for i in range(x):
        row = []

        for j in range(y):
            row.append(i * j)

        matrix.append(row)

    return matrix

print(two_dimensional_list(3, 5))
