a = int(input('введи а = '))
b = int(input('введи b = '))
c = int(input('введи c = '))
if a + b > c and b + c > a and a + c > b:
    # print('да')
    if a == b == c:  # a == b and b == c:
        print('треугольник равносторонний')
    elif a == b or b == c or c == a:
        print('треугольник равнобедренный')
    elif a*a + b*b == c*c or c*c + b*b == a*a or a*a + c*c == b*b:
        print('треугольник прямоугольный')
    else:
        print('треугольник произвольный')
else:
    print('нет')
