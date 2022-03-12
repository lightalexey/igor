a = int(input())
s = int(input())
b = ''
while a > 0:
    r = str(a % s)
    b = r + b
    a = a // s
print(b)