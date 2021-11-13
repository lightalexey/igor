from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(11)-5)
    print(a[i], end=' ')
print()
# решение начинается отсюда...

imax = 0
kimax = 0
for i in range(n):
    if a[i] >= a[imax]:
        imax = i
for i in range(n):
    if a[i] == a[imax]:
        kimax += 1

print('max[', imax, ']=', a[imax], kimax)
