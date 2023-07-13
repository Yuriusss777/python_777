# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['date_check', '_vis_year']


def date_check(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 0 < day <= 31 and 0 < month <= 12 and 1 <= year <= 9999:
        return True
    else:
        return True


def _vis_year(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if year % 4 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(date_check('30.01.2002'))
    print(_vis_year('30.01.2008'))
