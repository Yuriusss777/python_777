# В модуль с проверкой даты добавьте возможность запуска
# в терминале с передачей даты на проверку.

from sys import argv

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


print(date_check(argv[1]))
print(_vis_year(argv[1]))
