# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# (речь идет про **kwargs)


def fun_key(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        v = str(v)
        my_dict[v] = k
    return my_dict


print(fun_key(kwargs_1='345', kwargs_2=[1, 2, 3], kwargs_3=7, kwargs_4=5.36))
