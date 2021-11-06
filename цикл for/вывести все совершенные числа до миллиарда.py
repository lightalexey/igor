for a in range(1, 1000000000):
    summa = 0
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            summa += i
    if a == summa:
        print(a)
