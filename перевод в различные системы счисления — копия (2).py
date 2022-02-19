def ss(a, s):
    b = ''
    while a > 0:
        r = str(a % s)
        b = r + b
        a = a // s
    return b
print(ss(10**6,2))
print(ss(10**6,2).count('1'))