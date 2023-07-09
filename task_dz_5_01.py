# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
#
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')


text = 'file:///C:/Users/Dolzh/OneDrive/%D0%A0%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9%20%D1%81%D1%82%D0%BE%D0%BB/python/main.py'

def my_func(*args):
    """функция, создающая кортеж из элементов: путь, имя файлоа, расширение файла"""
    res = text.split('/')
    last_elem = res.pop().split('.')
    new_res = '/'.join(res[0:-1])
    name = last_elem[0]
    expansion = last_elem[1]

    return new_res, name, expansion


print(my_func(text))




