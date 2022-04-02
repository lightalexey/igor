a = 100000000
b = 100000100
for i in range(a, b + 1):
    k = 0
    for n in range(2, int(a**0.5) + 1):
        if i % n == 0:
            k += 1
            if k >= 1:
                break
    if k == 0:
        print(i, end=' ')