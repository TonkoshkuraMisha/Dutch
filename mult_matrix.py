from out_matrix import *

m = int(input())

result = [[0] * m for _ in range(m)]

matrix1 = [list(map(int, input().split())) for _ in range(m)]
matrix2 = [list(map(int, input().split())) for _ in range(m)]

print_matrix(result, m)
print()
print_matrix(matrix1, m)
print()
print_matrix(matrix2, m)
print()

for i in range(m):
    for j in range(m):
        for k in range(m):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print_matrix(result, m)
