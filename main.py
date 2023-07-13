import numpy as np

# gorizont = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# vert = (1, 2, 3, 4, 5, 6, 7, 8)
# chess_board = []
# for i in gorizont:
#     for g in vert:
#         chess_board.append([i, g])
#
# print(chess_board)
#
# # free_cells_7 = chess_board
# f_1 = input('Введите координаты первого ферзя через пробел в фомате a 1: ')
# f_1_new = f_1.split(' ')
# g = f_1_new[0]
# v = f_1_new[1] = int(f_1_new[1])
# # f_1_new = tuple(f_1_new)
# print(f_1_new)
#
# for i in range(len(chess_board) - 1):
#     if f_1_new == chess_board[i]:
#         print(True)
#         chess_board.remove(chess_board[i])
#
#
#
#
# print(chess_board)

# #
# matrix = [[('a', 1), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('a', 6), ('a', 7), ('a', 8)],
#                [('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('b', 6), ('b', 7), ('b', 8)],
#                [('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('c', 6), ('c', 7), ('c', 8)],
#                [('d', 1), ('d', 2), ('d', 3), ('d', 4), ('d', 5), ('d', 6), ('d', 7), ('d', 8)],
#                [('e', 1), ('e', 2), ('e', 3), ('e', 4), ('e', 5), ('e', 6), ('e', 7), ('e', 8)],
#                [('f', 1), ('f', 2), ('f', 3), ('f', 4), ('f', 5), ('f', 6), ('f', 7), ('f', 8)],
#                [('g', 1), ('g', 2), ('g', 3), ('g', 4), ('g', 5), ('g', 6), ('g', 7), ('g', 8)],
#                [('h', 1), ('h', 2), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8)]]
# # )
# #
# #
# # print(np.diag(a))
#
# # matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
#
#
# # only works for diagnoals of equal width and height
# def forward_diagonal(matrix):
#     if not isinstance(matrix, list):
#         raise TypeError("Must be of type list")
#
#     results = []
#     x = 0
#     for k, row in enumerate(matrix):
#         # next diag is (x + 1, y + 1)
#         for i, elm in enumerate(row):
#
#             if i == 0 and k == 0:
#                 results.append(elm)
#                 break
#             if (x + 1 == i):
#                 results.append(elm)
#                 x = i
#                 break
#     return results
#
#
# print('forward diagnoals', forward_diagonal(matrix))


a: list = ([1, 2, 3, 4, 5])

b = ['a', 'b', 'c', 'd', 'e']

chess_board = []
for i in a:
    for g in b:
        el = str(i) + str(g)
        chess_board.append(el)
print(chess_board)



