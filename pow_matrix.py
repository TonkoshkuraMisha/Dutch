from out_matrix import *

m = int(input())
result = [[0] * m for _ in range(m)]

E = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        if i == j:
            E[i][j] = 1

matrix = [list(map(int, input().split())) for _ in range(m)]
p = int(input())
print_matrix(matrix, m)
print()


def mult(matrix1, matrix2):
    for i in range(m):
        for j in range(m):
            for k in range(m):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def power(matrix, p):
    if p == 1:
        return matrix
    elif p == 2:
        return mult(matrix, matrix)
    elif p == 3:
        return power(mult(matrix, matrix), p - 1)
    else:
        return power(mult(matrix, matrix), p - 2)


print_matrix(power(matrix, p), m)
