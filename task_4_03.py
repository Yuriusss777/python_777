# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введён


def create_unicode_dict(nums: str = '1 9') -> dict:
    """Формирует словарь, где ключ - символ из Unicode,
     а значение — целое число."""
    start, stop = map(int, nums.split())
    unicode_dict = {}
    for num in range(start, stop + 1):
        unicode_dict[ord(str(num))] = num
    return unicode_dict


print(create_unicode_dict())
