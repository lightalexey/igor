from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(101)-50)
    print(a[i], end=' ')
print()
#
summa = 0
for i in range(n):
    summa += a[i]
print(summa)
#
summa = 0
for i in a:
    summa += i
print(summa)