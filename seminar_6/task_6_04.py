# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

_tries_dict = {}


def zagad(text: str, ans_list: list[str], tries: int = 3) -> int:
    """Функция получает на вход загадку, список с возможными вариантами отгадок
       и количество попыток на угадывание.
       Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны."""

    print(text)
    count = 0
    ans_list = list(map(lambda x: x.lower(), ans_list))
    while tries > count:
        count += 1
        if input('Ответ на загадку: ').lower() in ans_list:
            return count
    return 0


def mnogo_zagad():
    ZAGADKI = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['Замок']
    }
    for key, value in ZAGADKI.items():
        create_counter_dict(key, zagad(key, value))


def create_counter_dict(text: str, tries: int):
    """подсчет попыток"""
    _tries_dict[text] = tries


def show_counter_dict():
    """просмотр попыток"""
    print('_' * 10, 'Ваши попытки', '_' * 10)
    for k, v in _tries_dict.items():
        print(k, v)


if __name__ == '__main__':
    mnogo_zagad()
    show_counter_dict()
