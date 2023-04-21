"""
Максимальная сумма
В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой.
Входные данные
В первой строке входных данных записано единственное число -  размер массива.
Во второй строке записано n целых чисел - сам массив.
Выходные данные
Выведите одно число - максимальную сумму на отрезке в данном массиве.
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
prefixes = [0] * (N + 1)
previous = 0

for i, number in enumerate(input().split()):
    previous += int(number)
    prefixes[i + 1] = previous
mn, mx = prefixes[0], prefixes[1]
mx_sum = prefixes[1]

for prefix in prefixes[2:]:
    if mx_sum < 0 and prefix < 0 and prefix > mx_sum:
        mx_sum = prefix
        mn, mx = prefix - mx_sum, prefix  ## !!! хрень
    elif prefix > mx:
        mx = prefix
    elif prefix < mn:
        if mx - mn > mx_sum:
            mx_sum = mx - mn
        mn, mx = prefix, prefix  ## !!! а надо по другому?
if mx - mn > mx_sum:
    mx_sum = mx - mn

print(str(mx_sum))
