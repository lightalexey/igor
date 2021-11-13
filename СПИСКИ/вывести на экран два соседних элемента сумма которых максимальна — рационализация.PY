from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(11)-5)
    print(a[i], end=' ')
print()
# решение начинается отсюда...

i1 = 0 # индекс из двух подряд идущих элементов сумма которых максимальна
for i in range(n-1):
    if a[i] + a[i+1] > a[i1] + a[i1+1]:
       i1 = i

print(a[i1], a[i1+1])