for a in range(45000000, 50000000):
    k = 0
    for i in range(1, a // 2 + 1, 2):
    # for i in range(1, round(a ** 0.5) + 1):
        if a % i == 0: # and i % 2 != 0:
            k += 1
            if k > 5:
                break
    if k == 5:
        print(a)
