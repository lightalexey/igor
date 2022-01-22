s = 'Мама мыла раму'
print('Первый элемент', s[0])
print('Последний элемент', s[-1])
print('количество символов', len(s))
print('2 способ последний элемент', s[len(s)-1])
kol_a = 0
for i in range(len(s)):
    if s[i] == 'а':
        kol_a += 1
print('Количество букв а равно', kol_a)
print('Количество букв а равно', s.count('а'))
print('Индекс первой буквы а', s.find('а'))
s = s.replace('раму', 'окно')
# print(s.replace('раму', 'окно'))
print(s)
