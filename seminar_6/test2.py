


gorizont = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
vert = (1, 2, 3, 4, 5, 6, 7, 8)
chess_board = []
for i in gorizont:
    for g in vert:
        chess_board.append((i, g))

print(chess_board)


free_cells_7 = []
f_1 = input('Введите координаты первого ферзя через пробел в фомате a 1: ')
f_1_new = f_1.split(' ')
g = f_1_new[0]
v = f_1_new[1] = int(f_1_new[1])
f_1_new = tuple(f_1_new)
print(f_1_new)
if f_1_new in chess_board:
    for i in range(len(gorizont))
else:
    print(False)

