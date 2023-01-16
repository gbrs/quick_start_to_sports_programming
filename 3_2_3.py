"""
Имеется калькулятор, который выполняет следующие операции:

Умножить число X на 2.
Умножить число X на 3.
Прибавить к числу X единицу.
Определите, какое наименьшее количество операций требуется,
чтобы получить из числа 1 число N
"""

"""
неправда, что из i // 3 всегда путь короче, чем из i // 2
"""


N = int(input())
lst = [0] * (N + 1)
for i in range(2, N + 1):
    variants = []
    if not i % 3:
        variants.append(lst[i // 3])
    if not i % 2:
        variants.append(lst[i // 2])
    variants.append(lst[i - 1])
    lst[i] = min(variants) + 1

# print(*lst)
print(lst[N])
