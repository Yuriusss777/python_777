import pickle
import os
import json
import csv


def my_func():
    """"рекурсивный обход директории и все вложенные директории"""
    a = []
    with open('dz.pickle', 'wb') as file:
        pickle.dump(a, file)
    # with open('dz1.json', 'w') as f:
    #     json.dump(a, f)

    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        a.append((len(path) - 1) * os.path.basename(root))
        # print((len(path) - 1) * os.path.basename(root))
        for file in files:
            a.append(len(path) * file)

    return file

print(my_func())
# with open('dz.pickle', 'rb') as f:
#     c = pickle.load(f)

# with open('dz.json', 'w') as f:
#     json.dump(c, f)

# print(c)
