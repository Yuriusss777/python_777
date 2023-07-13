import numpy as np

gorizont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vert: list = ([1, 2, 3, 4, 5, 6, 7, 8])
chess_board = []
for i in gorizont:
    for j in vert:
        el = str(i) + str(j)
        chess_board.append(el)
print(chess_board)

NUMBER = 8
chess_board_matrix = [chess_board[i: i + NUMBER] for i in range(0, len(chess_board), 8)]

print(chess_board_matrix)

chess_board_matrix_new = np.matrix(chess_board_matrix)

a = np.diag(chess_board_matrix_new)
b = np.diag(np.fliplr(chess_board_matrix_new))

print(a)
print(b)
f_1 = input('Введите координаты первого ферзя по формату а3: ')
if f_1 in np.diag(chess_board_matrix_new):
    print(True)
else:
    print(False)

# print(gorizont)
# matrix = []
# for i in range(len(gorizont[0])):
#     for g in range(len(gorizont[1])):
#         matrix.append(gorizont[i], gorizont[g])
#
# print(matrix)
