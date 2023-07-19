# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
# (решение задачи "не в одну строку" есть на 4 семинаре(5 задача))

TO_DECIMAL = 100
names = ['Alex', 'Mark', 'Anton', 'Mila']
salary = [50000, 70000, 120000, 65000]
extra = ['10.25%', '20.55%', '25.50%', '30.05%']


def extra_serializer(names: list[str], salary: list[int], extra: list[str]) -> dict[str: float]:
    return {name: sal / TO_DECIMAL * ext for name, sal, ext in
            zip(names, salary, (float(i[:-1]) for i in extra))}.items()


print(*(extra_serializer(names, salary, extra)))
