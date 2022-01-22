from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(11))
    print(a[i], end=' ')
print()
# решение начинается отсюда...
k = 0
for i in range(n-1):
    if a[i] % 2 == 0 and a[i+1] % 2 != 0:
        k += 1
    if a[i] % 2 != 0 and a[i+1] % 2 == 0:
        k += 1
print(k)


