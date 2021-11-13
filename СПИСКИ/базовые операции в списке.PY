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
p = 1
sum_pol = 0
sum_otr = 0
o = 0
kol = 0
k2 = 0
for i in range(n):
    summa += a[i]  # summa = summa + a[i]
    p *= a[i]
    if a[i] > 0:
        kol += 1
        sum_pol += a[i]
    if a[i] < 0:
        sum_otr += a[i]
    if a[i] == 0:
        o += 1
    if a[i] % 2 == 0:
        k2 +=1


print('Сумма элементов списка равна', summa)
print('произведение равно: ', p)
print(summa/n)
print('Сумма положительных элементов равна', sum_pol)
print('Сумма отрицательных элементов равна', sum_otr)
print(o)
print(kol)
print(a[0])
print(a[n-1])
print(a[-1])
print(k2)