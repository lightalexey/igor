f = open('24_demo.txt')
s = f.readline()
# print(len(s))
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
otvet = 1
k = 1
for i in range(len(s) - 1):
    if s[i] != s[i+1]:  # Текущая цепочка растёт...
        k += 1
    else: # цепочка оборвалась
        if k > otvet:
            otvet = k
        k = 1
#if k > otvet:
#    otvet = k
print(max(otvet, k))