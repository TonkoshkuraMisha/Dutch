# This function add matrix
def matrix_add(mx1: list, mx2: list):
    if len(mx1) == len(mx2):
        n = len(mx1[0])
        matrix = [[0] * m1]* n
        for i in range(m1):
            for j in range(n):
                matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    else:
        print("You must add equal lens matrix")
    return matrix


m1 = int(input())
matrix1 = [list(map(int, input().split())) for _ in range(m1)]
m2 = m1
matrix2 = [list(map(int, input().split())) for _ in range(m2)]

result = matrix_add(matrix1, matrix2)
print(result)
