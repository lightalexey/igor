# Пользователь вводит три различных числа, вывести максимальное.
a = int(input('введи а = '))
b = int(input('введи b = '))
c = int(input('введи c = '))
if c < a > b: print(a)
if c < b > a: print(b)
if a < c > b: print(c)
# еще способ...
print(max(a, b, c))
