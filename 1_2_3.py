"""
Два максимума.
Дан массив (хитрым образом рассчитываемый). Вам требуется определить позиции первого максимума и второго максимума.
"""

'''
комментаторы пишут, что питон не проходит по времени. Преподаватели, вроде, соглашаются
'''



MOD = 1791791791

N = int(input())
cur, a, b = map(int, input().split())

mx1 = -1
mx1_pos = -1
mx2 = -1
mx2_pos = -1

for i in range(N):
    cur = (a * cur + b) % MOD
    if cur > mx1:
        mx2 = mx1
        mx2_pos = mx1_pos
        mx1 = cur
        mx1_pos = i
    elif cur > mx2:
        mx2 = cur
        mx2_pos = i

print(mx1_pos + 1, mx2_pos + 1)
