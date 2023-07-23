# 1. Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def matrix(array):
    trans_matrix = [[0 for j in range(len(array))] for i in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            trans_matrix[j][i] = array[i][j]

    return trans_matrix


list_my = [[1, 2, 3], [4, 5, 6]]
print(matrix(list_my))
