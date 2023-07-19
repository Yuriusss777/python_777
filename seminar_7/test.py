text = ['как понять эти функции',
        'очень сложно']

with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    print(f.truncate())
