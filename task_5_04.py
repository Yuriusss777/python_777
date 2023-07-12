# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


res = []
for i in range(101):
    if sum(map(int, list(str(i)))) != 8:
        res.append(i)

print(res)

# решение в одну строку
res_new = [i for i in range(101) if sum(map(int, list(str(i)))) != 8]

print(res_new)
