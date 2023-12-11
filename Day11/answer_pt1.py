import numpy as np

f = open("Day11/input.txt", "r").readlines()

a = []
m = []
for i in f:
    for j in i:
        if j != "\n":
            a.append(j)
    m.append(a)
    a = []

matrix = np.array(m)

i = 0
while i < len(matrix.T):
    if all(j == '.' for j in matrix.T[i]):
        matrix = np.insert(matrix, i, '.', axis = 1)
        i += 2
    else:
        i += 1

i = 0
while i < len(matrix):
    if all(j == '.' for j in matrix[i]):
        matrix = np.insert(matrix, i, '.', axis = 0)
        i += 2
    else:
        i += 1

# print(matrix)

pos = []

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "#":
            pos.append((r,c))

# print(pos)

total = 0

for i in range(len(pos)):
    for j in range(i+1, len(pos)):
        x_dist = abs(pos[i][0] - pos[j][0])
        y_dist = abs(pos[i][1] - pos[j][1])

        # print(pos[i], pos[j], x_dist + y_dist)

        total += x_dist + y_dist
print(total)