# Пользователь вводит три различных числа, вывести максимальное.
a = int(input('введи а = '))
b = int(input('введи b = '))
c = int(input('введи c = '))
if a > b and a > c:
    print('самое большое число - a=', a)
elif b > a and b > c:
    print('самое большое число - b=', b)
else:
    print('самое большое число - c=', c)
