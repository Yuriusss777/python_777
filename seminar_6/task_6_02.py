# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте
# генераторное выражение.

from random import randint
from sys import argv


def ugadaika(start: int, stop: int, tries: int) -> bool:
    """Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
        Внутри генерируется случайное число в указанных границах
        и пользователь должен угадать его за заданное число попыток."""

    random_num = randint(start, stop)
    while tries > 0:
        usr_try = int(input('Число: '))
        if usr_try > random_num:
            print('less')
        elif usr_try < random_num:
            print('greater')
        else:
            print('угадали')
            return True
        tries -= 1
    return False


if __name__ == '__main__':
    FIRST_ARG = 1
    TRIRD_ARG = 4
    st, end, tr, = tuple(map(int, argv[FIRST_ARG:TRIRD_ARG]))
    print(ugadaika(st, end, tr))
