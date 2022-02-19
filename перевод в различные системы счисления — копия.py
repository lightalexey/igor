a = 9**8 + 3**5 - 9
s = 3
b = ''
while a > 0:
    b = str(a % s) + b
    a //= s
print(b)
print(b.count('2'))