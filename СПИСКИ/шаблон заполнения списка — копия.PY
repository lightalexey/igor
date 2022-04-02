from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(11))
    print(a[i], end=' ')
print()
# решение начинается отсюда...
p = 0
for i in range(n - 1):
    if (a[i] + a[i+1]) % 2 == 0 and (a[i] % 2 != 0 or a[i+1] % 2 != 0):
        p += 1
print(p)