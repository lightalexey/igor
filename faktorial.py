n = int(input())
nn = n
f = 1
while (n - 1) != 0:
    f = f * n
    n = n - 1
print(f)
f = 1
for i in range(1, nn + 1):
    f *= i
print(f)
f = 1
for i in range(nn, 1, -1):
    f *= i
print(f)