f = open('разделенный на строки Тургенев.txt')
name = f.readline()
text = f.read()
print('Название произведения:', name)
print('------------------------')
print(text)
print(len(text))
print(text.count('о'))


