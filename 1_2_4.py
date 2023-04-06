"""
Префиксные суммы
В этой задаче вам нужно будет много раз отвечать на запрос <<Найдите сумму чисел на отрезке в массиве>>.
Входные данные
В первой строке записано два целых числа - размер массива и количество запросов.
Во второй строке записаны n целых чисел - сам массив.
Далее в q строках описаны запросы к массиву. Каждый запрос описывается двумя числами -
левой и правой границей отрезка, на котором нужно найти сумму.
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, Q = map(int, input().split())
prefixes = [0] * (N + 1)
previous = 0
for i, number in enumerate(input().split()):
    previous += int(number)
    prefixes[i + 1] = previous
for i in range(Q):
    l, r = map(int, input().split())
    print(str(prefixes[r] - prefixes[l - 1]) + '\n')


