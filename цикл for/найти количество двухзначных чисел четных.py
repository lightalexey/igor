k = 0
k2 = 0
k3 = 0
k5 = 0
summa = 0
for i in range(10, 99 + 1):
    summa += i
    k += 1
    if i % 2 == 0:
        k2 += 1
    if i % 3 == 0:
        k3 += 1
    if i % 5 == 0:
        k5 += 1
print('количество двузначных четных чисел', k2)
print(k3)
print(k5)
print(k)
print(summa)
