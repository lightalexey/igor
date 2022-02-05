a = int(input())
n = a
k = 0
sum = 0
while a > 0:
    b = a % 10
    sum += b
    a = a // 10
    k += 1
print(sum, k, n % 10)