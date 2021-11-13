from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(11)-5)
    print(a[i], end=' ')
print()
# решение начинается отсюда...
sum = -101
for i in range(n-1):
    if a[i] + a[i+1] > sum:
        sum = a[i] + a[i+1]
        a1 = a[i]
        a2 = a[i+1]

print(a1, a2)