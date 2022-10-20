"""
Кузнечик
Перед клетчатой полоской длины n сидит кузнечик. В каждой клетке написано
целое число. Когда кузнечик оказывается в какой-то клетке, ему дают конфет
в том количестве, которое записано в этой клетке. Кузнечик умеет прыгать
на следующую ступеньку, а также через одну. Помогите кузнечику - определите,
какое максимальное количество конфет он может съесть, если в итоге кузнечик
должен оказаться в последней клетке? Обратите внимание, количество конфет
может быть отрицательно.
Входные данные
В первой строке записано единственное целое число n - длина полоски.
Во второй строке записано n целых чисел a_i - количество конфет в каждой клетке.
Выходные данные
Выведите одно число - максимальное количество конфет, которое может собрать кузнечик.
"""


N = int(input())
lst = list(map(int, input().split()))
lst.insert(0, 0)  # количество конфет, когда он стоит на полу перед лестницей

for i in range(2, N + 1):
    lst[i] = lst[i] + max(lst[i - 1], lst[i - 2])

print(lst[-1])
