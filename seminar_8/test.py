import pickle
import os
import json
import csv


def my_func():
    """"рекурсивный обход директории и все вложенные директории"""
    a = []
    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        a.append((len(path) - 1) * os.path.basename(root))
        for file in files:
            a.append(len(path) * file)
    return a


# c = [1, 2, 3, 4, 5]
with open('dz.pickle', 'wb') as file:
    pickle.dump(my_func(), file)
with open('dz1.json', 'w') as f1:
    json.dump(my_func(), f1)
with open('dz1.csv', 'w') as f2:
    b = csv.writer(f2)
    b.writerow(my_func())


# with open('dz.pickle', 'rb') as f:
#     print(pickle.load(f))
#
#
# with open('dz1.json', 'r') as f:
#     print(json.load(f))
#
# with open('dz1.csv', 'r') as f:
#     c = csv.reader(f)
#     for line in c:
#         print(line)

print(my_func())
