from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(101)-50)
    print(a[i], end=' ')
print()
# решение начинается отсюда...
summa = 0
k = 0
for i in range(n):
    if a[i] > 0 and a[i] % 2 == 0:
        summa += a[i]
        k += 1
print(summa/k)