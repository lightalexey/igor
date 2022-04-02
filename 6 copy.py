a = 100
b = 200
for i in range(a, b + 1):
    k = True
    for n in range(2, a//2 + 1):
        if i % n == 0:
            k = False
            break
    if k:
        print(i, end=' ')