# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


from typing import Iterator


def prime(n: int) -> Iterator[int]:
    """Генератор простых чисел."""
    count = 1
    prime_num = 2
    yield prime_num
    while count < n:
        prime_num += 1
        for i in range(2, prime_num//2 + 1):
            if prime_num % i == 0:
                break
        else:
            count += 1
            yield prime_num


for num in prime(10):
    print(num)