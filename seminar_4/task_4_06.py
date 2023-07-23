#  Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def index_by_sum(nums: list[int], start: int, end: int) -> int:
    if end < start:
        end, start = start, end
    if end > len(nums):
        end = len(nums) - 1
    if start < 0:
        start = 0
    return sum(nums[start:end + 1])


num_list = [1, 2, 3, 1, 2, 3]
print(index_by_sum(num_list, 0, 6))
