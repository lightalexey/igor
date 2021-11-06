a, summa = int(input('введи число:')), 0
for i in range(1, a // 2 + 1):
    if a % i == 0:
        summa += i
if a == summa:
    print('да')
else:
    print('нет')