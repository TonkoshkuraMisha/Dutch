from out_matrix import *


def transpose(matrix):
    res = []
    n = len(matrix)
    m = len(matrix[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matrix[i][j]]
        res = res + [tmp]
    return res


m = int(input())
matrix1 = [list(map(int, input().split())) for _ in range(m)]

t_matrix = transpose(matrix1)
print_matrix(t_matrix, m)
