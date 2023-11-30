# -- coding: utf-8 --
#вариант 8

def divide_diagonal(matrix, k):
    n = len(matrix)
    if k <= 0 or k > n:
        raise ValueError("Неверное значение K")
    diagonal_element = matrix[k-1][k-1]
    if diagonal_element == 0:
        raise ValueError("Диагональный элемент равен нулю")
    for j in range(n):
        matrix[k-1][j] /= diagonal_element

    return matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
k = 2
result = divide_diagonal(matrix, k)
print(result)