import math


def rectang(a, b):
    s = a * b
    return s


def triang(a, h):
    s = 1 / 2 * a * h
    return s


def circle(r):
    s = round(math.pi, 2) * r ** 2
    return s


print('Площадь какой фигуры вы хотели бы найти?')
ch = int(input('1 - прямоугольник, 2 - треугольник, 3 - круг: '))
match ch:
    case 1:
        a, b = int(input('Введите длину: ')), int(input('Введите ширину: '))
        print(rectang(a, b))
    case 2:
        a, h = int(input('Введите основание: ')), int(input('Введите высоту: '))
        print(triang(a, h))
    case 3:
        r = int(input('радиус круга: '))
        print(circle(r))