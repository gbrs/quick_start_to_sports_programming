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
mx_sum = 0

for prefix in prefixes[2:]:
    if prefix > mx:
        mx = prefix
    if prefix < mn:
        if mx - mn > mx_sum:
            mx_sum = mx - mn
        mn, mx = prefix, prefix
if mx - mn > mx_sum:
    mx_sum = mx - mn

print(str(mx_sum))
