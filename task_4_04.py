# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку


def buble_sort(nums: list[int]) -> list[int]:
    """Сортировка пузырьком"""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(buble_sort([1, 3, 2, 5]))