from out_matrix import *
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)


def power(matrix, p):
    r = mult(matrix, matrix_stable)
    if p == 1:
        return matrix
    elif p == 2:
        return r
    else:
        return power(r, p - 1)


def mult(matrix1, matrix2):
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


# Вводим размерность квадратной матрицы
m = int(input())

# Вводим строки матрицы
matrix = [list(map(int, input().split())) for _ in range(m)]

# Вводим степень, в которую возводим матрицу
p = int(input())

print_matrix(matrix, m)
print()

matrix_stable = matrix
result = power(matrix, p)
print_matrix(result, m)
