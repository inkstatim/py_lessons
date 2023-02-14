a, b = map(int, input().split())

matrix = [['.'] * b for _ in range(a)]

for i in range(a):
    for j in range(b):
        if (i + j) % 2 == 1:
            matrix[i][j] = '*'
for i in matrix:
    print(*i)
