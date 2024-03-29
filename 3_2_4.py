"""
Перед клетчатой полоской длины n сидит кузнечик.
Каждая клетка является либо занятой, либо свободной.
Кузнечик умеет прыгать на 1, 2 и 3 клетки вперед.
Найдите количество различных путей,
которыми он может добраться до последней клетки, не заходя в занятые.

Входные данные. В первой строке записано единственное целое число n.
Во второй строке записана строка длины n, состоящая только из нулей и единиц.
Ноль обозначает свободную клетку, а единица - занятую.

Выходные данные. Выведите единственное число - количество способов добраться
до последней клетки. Поскольку это число может быть очень большим,
выведите его по модулю 10^9 + 7
"""

"""
Красивое решение: помнить, что нам не нужно весь список таскать - 
нам нужно помнить только три последние элемента.
p = 10 ** 9 + 7
x = (0, 0, 1)
n = int(input())
for item in map(int, input()):
    if not item:
        x = (x[1], x[2], (x[0] + x[1] + x[2]) % p)
    else:
        x = (x[1], x[2], 0)
print(x[2])
"""


N = int(input())
stairs = list(map(int, input()))
stairs.insert(0, 0)  # место под лестницей, где сидит кузнечик
counter = [0] * (N + 1)

if stairs[1] == 0:
    counter[1] = 1
if N > 1 and stairs[2] == 0:
    counter[2] = 1 + counter[1]
if N > 2 and stairs[3] == 0:
    counter[3] = 1 + counter[1] + counter[2]

for i in range(4, N + 1):  # даже не запустится при N < 4
    if stairs[i] == 0:
        counter[i] = (counter[i - 3] + counter[i - 2] + counter[i - 1]) % (10**9 + 7)

print(counter[N] % (10**9 + 7))
