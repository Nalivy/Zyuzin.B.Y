# -- coding: utf-8 --
#вариант 8

def transpose_matrix(matrix):
    transposed_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
            
    return transposed_matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)