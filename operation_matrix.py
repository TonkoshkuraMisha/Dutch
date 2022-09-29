from out_matrix import *


def operation_on_matrix(sign: str):
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
            result[i][j] = eval(f"{matrix1[i][j]}{sign}{matrix2[i][j]}")

    print_matrix(result, m)
